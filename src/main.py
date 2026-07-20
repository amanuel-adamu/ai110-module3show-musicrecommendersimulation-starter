"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

import textwrap

from src.recommender import load_songs, recommend_songs


# Three distinct taste profiles to test the recommender against.
# Each maps a display name to the user_prefs dict score_song() expects.
PROFILES = {
    "High-Energy Pop": {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.9,
    },
    "Chill Lofi": {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.4,
    },
    "Deep Intense Rock": {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.9,
    },
}


# Column headers and widths (characters) for the recommendations table.
_HEADERS = ["#", "Title", "Artist", "Score", "Why (reasons)"]
_WIDTHS = [2, 20, 16, 5, 46]


def _print_row(cells: list) -> None:
    """Print one table row. Each cell is a list of text lines (for wrapping)."""
    height = max(len(c) for c in cells)
    for i in range(height):
        parts = []
        for cell, width in zip(cells, _WIDTHS):
            text = cell[i] if i < len(cell) else ""
            parts.append(" " + text.ljust(width) + " ")
        print("|" + "|".join(parts) + "|")


def _separator() -> None:
    """Print a +---+---+ separator line matching the column widths."""
    print("+" + "+".join("-" * (w + 2) for w in _WIDTHS) + "+")


def print_recommendations(name: str, user_prefs: dict, songs: list, k: int = 5) -> None:
    """Print the top k recommendations for one profile as a formatted table."""
    recommendations = recommend_songs(user_prefs, songs, k=k)

    print()
    print(
        f"TOP {k} RECOMMENDATIONS - {name}  "
        f"({user_prefs['favorite_genre']} / {user_prefs['favorite_mood']} / "
        f"energy ~{user_prefs['target_energy']})"
    )

    _separator()
    _print_row([[h] for h in _HEADERS])
    _separator()

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        # Wrap each reason to the "Why" column width so it stays inside the cell.
        why_lines = []
        for reason in explanation.split("; "):
            why_lines.extend(textwrap.wrap(reason, _WIDTHS[4]))

        cells = [
            [str(rank)],
            textwrap.wrap(song["title"], _WIDTHS[1]) or [""],
            textwrap.wrap(song["artist"], _WIDTHS[2]) or [""],
            [f"{score:.2f}"],
            why_lines or [""],
        ]
        _print_row(cells)
        _separator()


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Run the recommender for each distinct profile.
    for name, user_prefs in PROFILES.items():
        print_recommendations(name, user_prefs, songs)


if __name__ == "__main__":
    main()
