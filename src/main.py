"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Default taste profile: "pop / happy" listener
    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.8,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    # Header describing who we recommended for
    print()
    print("=" * 44)
    print("  TOP RECOMMENDATIONS")
    print(
        f"  for a {user_prefs['favorite_genre']} / "
        f"{user_prefs['favorite_mood']} listener "
        f"(energy ~{user_prefs['target_energy']})"
    )
    print("=" * 44)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n{rank}. {song['title']} - {song['artist']}")
        print(f"   Score: {score:.2f} / 4.0")
        print("   Why:")
        # explanation is the reasons joined by "; " - split back out for bullets
        for reason in explanation.split("; "):
            print(f"     - {reason}")
    print()


if __name__ == "__main__":
    main()
