"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    profiles = {
        "Happy J-Pop": {
            "genre": "j-pop",
            "mood": "happy",
            "energy": 0.75,
            },
        "Intense K-Pop": {
        "genre": "k-pop",
        "mood": "intense",
        "energy": 0.40,},
    
        "Chill Pop": {
        "genre": "pop",
        "mood": "chill",
        "energy": 0.85,
        },
    
        "Focused Lofi": {
            "genre": "lofi",
            "mood": "focused",
            "energy": 0.35,
        },
    }
    
    for profile_name, user_prefs in profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print("================================================================================\n")
        print(f"Profile: {profile_name}")
        print(
            f"Preferences: genre={user_prefs['genre']}, "
            f"mood={user_prefs['mood']}, "
            f"energy={user_prefs['energy']}"
        )
        print("\nTop recommendations:\n")

        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}/4.00")
            print(f"Because: {explanation}")
            print()
    print("================================================================================")

if __name__ == "__main__":
    main()
