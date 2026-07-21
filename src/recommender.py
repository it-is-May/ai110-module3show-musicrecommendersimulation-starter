from typing import List, Dict, Tuple
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
        """Stores songs available to the recommender."""
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Returns top k songs ranked by user preference score."""
        def score(song: Song) -> float:
            total = 0.0
            if song.mood.strip().casefold() == user.favorite_mood.strip().casefold():
                total += 2.0
            if song.genre.strip().casefold() == user.favorite_genre.strip().casefold():
                total += 1.0
            total += 1 - abs(song.energy - user.target_energy)
            return total

        ranked = sorted(self.songs, key=score, reverse=True)
        return ranked[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explains why a song matches the user's preferences."""
        reasons: List[str] = []
        if song.mood.strip().casefold() == user.favorite_mood.strip().casefold():
            reasons.append("Mood match (+2.0)")
        if song.genre.strip().casefold() == user.favorite_genre.strip().casefold():
            reasons.append("Genre match (+1.0)")
        energy_sim = 1 - abs(song.energy - user.target_energy)
        reasons.append(f"Energy similarity (+{energy_sim:.2f})")
        return "; ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    import csv

    float_fields = ("energy", "tempo_bpm", "valence", "danceability", "acousticness")
    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            for field in float_fields:
                row[field] = float(row[field])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons: List[str] = []
    # Turning mood & genre into case-insensitive to enhance comparison
    if song["mood"].strip().casefold() == user_prefs["mood"].strip().casefold():
        score += 2.0
        reasons.append("Mood match (+2.0)")

    if song["genre"].strip().casefold() == user_prefs["genre"].strip().casefold():
        score += 1.0
        reasons.append("Genre match (+1.0)")

    energy_sim = 1 - abs(song["energy"] - user_prefs["energy"])
    score += energy_sim
    reasons.append(f"Energy similarity (+{energy_sim:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    results: List[Tuple[Dict, float, str]] = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        results.append((song, score, explanation))

    results.sort(key=lambda item: item[1], reverse=True)
    return results[:k]
