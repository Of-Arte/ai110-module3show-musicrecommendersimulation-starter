# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeFinder 1.0**

---

## 2. Intended Use

VibeFinder 1.0 is a music recommendation system designed to simulate how streaming platforms match user preferences to songs.

- **Generated Output**: Ranked lists of songs with breakdowns explaining why each song was selected.
- **User Assumptions**: Assumes the user can specify target preferences (favorite genre, mood, target energy, and acoustic instrument preference).
- **Target Audience**: Designed for exploration and algorithmic evaluation, not for production use.

---

## 3. How the Model Works

VibeFinder 1.0 uses a content-based scoring algorithm that evaluates songs one by one:

- **Song Attributes**: Analyzes categorical traits (genre, mood) and numerical traits (energy, acousticness, valence).
- **User Preferences**: Accepts target values for favorite genre, favorite mood, energy level (0.0 to 1.0), and acoustic preference (acoustic vs. electronic).
- **Scoring Rule**:
  - Awards **+3.0 points** for an exact genre match.
  - Awards **+2.0 points** for a matching mood.
  - Awards up to **+2.0 points** based on how close the song's energy is to the user's target energy.
  - Awards up to **+1.5 points** based on how closely the song's acousticness aligns with the user's preference.
  - Awards a **+0.5 point bonus** for happy, positive songs.
- **Ranking Rule**: Tracks are sorted from highest to lowest score, and the top tracks are returned to the user.

---

## 4. Data

- **Catalog Size**: 18 songs loaded from data/songs.csv.
- **Genre Coverage**: Pop, Indie Pop, Lofi, Rock, Metal, Reggae, Hip Hop, Blues, EDM, Folk, World, Jazz, Ambient, and Classical.
- **Data Attributes**: Each entry includes title, artist, genre, mood, energy, tempo_bpm, valence, danceability, and acousticness.
- **Missing Elements**: The dataset does not include audio recordings, lyrics, language tags, user listening history, or release dates.

---

## 5. Strengths

- **High Transparency & Explainability**: Every recommendation includes a step-by-step breakdown of how points were awarded.
- **Accurate Vibe Matching**: For distinct listener profiles, top recommendations align strongly with human intuition.
- **Predictable Behavior**: Deterministic scoring makes it easy to test and debug ranking logic.

---

## 6. Limitations and Bias

- **Catalog Size Constraint**: With only 18 songs, recommendations can feel repetitive.
- **Genre Dominance Bias**: Because genre matches receive a heavy point weight (+3.0), the system may ignore great songs from other genres that match the user's energy and mood perfectly.
- **Lack of Deep Audio Understanding**: The model relies on static CSV metadata rather than analyzing actual audio frequencies or song structure.
- **Filter Bubble Risk**: Users are repeatedly shown content inside their narrow preference parameters, missing out on musical discovery.

---

## 7. Evaluation

- **Tested Profiles**:
  1. Upbeat Pop Lover (genre: pop, mood: happy, energy: 0.8) -> Top result: Sunrise City (Score 8.69)
  2. Chill Lofi Listener (genre: lofi, mood: chill, energy: 0.35) -> Top result: Library Rain (Score 8.29)
  3. High Energy Workout (genre: rock, mood: intense, energy: 0.95) -> Top result: Storm Runner (Score 8.27)
- **Observations**: Shifting the point weight from genre to energy dramatically changed rankings, proving how algorithmic weights control recommendations.
- **Profile Comparisons**:
  - EDM vs. Acoustic Folk: The EDM profile favors high energy synthesized beats, while the acoustic folk profile shifts recommendations toward low-energy acoustic instrumentation.
  - Rock vs. Pop: High-energy rock profiles prioritize intensity and genre over calm tracks, showing that energy distance penalties successfully penalize mismatched vibes.

---

## 8. Future Work

- Add support for listening history to be factored into recommendations
- Add support for user feedback (thumbs up/down) to be factored into recommendations
- Add more context to the explanations, such as the user's listening history

---

## 9. Personal Reflection

- Building VibeFinder showed me how music streaming platforms translate human preferences into concrete mathematical scores.
- I was surprised that adjusting the weights of the scoring algorithm could have such a dramatic impact on the recommendations.
- I have a deeper appreciation for recommendation systems and the challenges of creating a system that balances personalization with discovery.
