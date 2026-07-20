"""
Command line runner for the Music Recommender Simulation.

This file runs the recommendation engine across multiple user taste profiles
and displays ranked results with plain language scoring breakdowns.
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded {len(songs)} songs from data/songs.csv.\n")

    profiles = [
        {
            "name": "Upbeat Pop Lover",
            "prefs": {"genre": "pop", "mood": "happy", "energy": 0.8, "likes_acoustic": False}
        },
        {
            "name": "Chill Lofi Listener",
            "prefs": {"genre": "lofi", "mood": "chill", "energy": 0.35, "likes_acoustic": True}
        },
        {
            "name": "High Energy Workout / Rock",
            "prefs": {"genre": "rock", "mood": "intense", "energy": 0.95, "likes_acoustic": False}
        }
    ]

    for prof in profiles:
        print("=" * 60)
        print(f"Profile: {prof['name']}")
        print(f"Preferences: {prof['prefs']}")
        print("-" * 60)
        recommendations = recommend_songs(prof["prefs"], songs, k=3)
        for rank, (song, score, explanation) in enumerate(recommendations, 1):
            print(f"{rank}. {song['title']} by {song['artist']} [{song['genre'].upper()}] - Score: {score:.2f}")
            print(f"   Reasons: {explanation}")
        print()


if __name__ == "__main__":
    main()

