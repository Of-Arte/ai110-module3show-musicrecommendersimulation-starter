# 🎵 Music Recommender Simulation

## Project Summary

VibeFinder 1.0 is a music recommendation engine designed to connect a user's personal taste profile with matching songs in a playlist. This simulation compares song characteristics—such as genre, mood, energy level, acoustic attributes, and valence—against user preferences. The system computes a numeric score for every track and presents a ranked list of top recommendations with reasons for each suggestion.

---

## How The System Works

Our music recommender turns raw data into personalized suggestions through a two-step process: **Scoring** individual songs and **Ranking** the catalog.

### 1. Data Representation

- **Song Attributes**: Every track in `data/songs.csv` contains structured features:
  - `genre` (pop, lofi, rock, jazz, edm, classical, metal, reggae, hip hop, blues, folk, world)
  - `mood` (happy, chill, intense, focused, aggressive, dramatic, nostalgic)
  - `energy` (scale from 0.0 for calm to 1.0 for high intensity)
  - `acousticness` (scale from 0.0 for electronic to 1.0 for acoustic instruments)
  - `valence` (measure of musical positivity from 0.0 gloomy to 1.0 upbeat)
  - `tempo_bpm` & `danceability` (rhythmic attributes)

- **User Taste Profile**: A user's preference profile stores:
  - `favorite_genre`: The listener's preferred style of music.
  - `favorite_mood`: The desired emotional vibe.
  - `target_energy`: Desired intensity level on a 0.0 to 1.0 scale.
  - `likes_acoustic`: Boolean flag (True/False) indicating preference for acoustic versus electronic instruments.

---

### 2. Algorithm Recipe (Scoring Rule)

To evaluate how well a song fits a user's profile, the system computes a numeric score using a multi-attribute point system:

1. **Genre Match** (+3.0 max points):
   - Exact Match: +3.0 points if the song's genre matches favorite_genre exactly.
   - Partial Match: +1.5 points if sub-genres overlap (e.g., "indie pop" matching "pop").
2. **Mood Match** (+2.0 points):
   - +2.0 points if the song's mood matches favorite_mood.
3. **Energy Proximity** (+2.0 max points):
   - Calculates energy difference: `distance = |song_energy - target_energy|`.
   - Proximity score: `2.0 * (1.0 - distance)`. A track with identical energy gains +2.0 points, while larger differences receive proportionately fewer points.
4. **Acoustic Preference** (+1.5 max points):
   - If likes_acoustic is True: `1.5 * song_acousticness`.
   - If likes_acoustic is False: `1.5 * (1.0 - song_acousticness)`.
5. **Upbeat Vibe Bonus** (+0.5 points):
   - +0.5 points if the user wants a "happy" mood and the song has high valence (>= 0.7).

The individual points are added together to yield the final track score along with plain-language explanation tags.

---

### 3. Recommendation Process (Ranking Rule)

1. **Catalog Scanning**: The system loops through all songs loaded from data/songs.csv.
2. **Scoring**: The score_song function evaluates each track and generates its total score and explanation breakdown.
3. **Sorting**: The songs are sorted in descending order by their numeric score (`sorted(key=score, reverse=True)`).
4. **Selection**: The system selects the top k highest-scoring tracks (default k=3 or k=5) to display to the user.

### Potential Bias Note

Because genre matches carry heavy point values (+3.0), this scoring logic might over-prioritize genre, ignoring great songs in adjacent genres that match the user's mood or energy perfectly.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows
   ```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

