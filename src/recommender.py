import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file into a list of dictionaries.

    Numeric columns are converted so later scoring can do math:
      - id, tempo_bpm  -> int
      - energy, valence, danceability, acousticness -> float
    All other columns (title, artist, genre, mood) stay as strings.

    Required by src/main.py
    """
    int_fields = {"id", "tempo_bpm"}
    float_fields = {"energy", "valence", "danceability", "acousticness"}

    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            song: Dict = {}
            for key, value in row.items():
                if key in int_fields:
                    song[key] = int(value)
                elif key in float_fields:
                    song[key] = float(value)
                else:
                    song[key] = value
            songs.append(song)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences (the Algorithm Recipe).

    Rules (max score = 4.0):
      - Genre match      -> +2.0   (strongest signal: sets the "lane")
      - Mood match       -> +1.0
      - Energy similarity -> +0.0 to +1.0, rewarding closeness to the target:
                             1 - abs(target_energy - song_energy)

    Expects user_prefs with keys: favorite_genre, favorite_mood, target_energy.
    Returns (score, reasons) where reasons explains where the points came from.

    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons: List[str] = []

    # Rule 1 — Genre match (+2.0)
    if song["genre"] == user_prefs["favorite_genre"]:
        score += 2.0
        reasons.append(f"genre match: {song['genre']} (+2.0)")

    # Rule 2 — Mood match (+1.0)
    if song["mood"] == user_prefs["favorite_mood"]:
        score += 1.0
        reasons.append(f"mood match: {song['mood']} (+1.0)")

    # Rule 3 — Energy similarity (0.0 to 1.0, graded by closeness)
    energy_similarity = 1 - abs(user_prefs["target_energy"] - song["energy"])
    score += energy_similarity
    reasons.append(
        f"energy {song['energy']} close to target "
        f"{user_prefs['target_energy']} (+{energy_similarity:.2f})"
    )

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Ranks the whole catalog and returns the top k recommendations.

    Steps:
      1. Judge every song with score_song() to get (score, reasons).
      2. Sort all songs by score, highest first.
      3. Return the top k as (song, score, explanation) tuples.

    Required by src/main.py
    """
    # 1. Score every song. score_song returns (score, reasons); we join the
    #    reasons list into a single explanation string for display.
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        scored.append((song, score, explanation))

    # 2. Rank highest-to-lowest. sorted() returns a NEW list and leaves the
    #    caller's `songs` list untouched. key = the score (index 1 of the tuple).
    ranked = sorted(scored, key=lambda item: item[1], reverse=True)

    # 3. Return only the top k.
    return ranked[:k]
