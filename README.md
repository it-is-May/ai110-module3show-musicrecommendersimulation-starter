# 🎵 Music Recommender Simulation

## Project Summary

This project is a small content-based music recommender. It compares a user's preferred genre, mood, and target energy with a catalog of 15 songs. Each song receives a weighted score, and the five highest-scoring songs are returned with explanations. I tested the system with multiple user profiles and examined how scoring weights, subjective labels, and uneven data affected the results.

---

## How The System Works

In real-world music platforms, recommendation systems may use collaborative filtering, content-based filtering, or a combination of both. Collaborative filtering uses behavior from many users, such as likes, skips, playlists, and listening history. Content-based filtering compares a user's preferences with song attributes such as genre, mood, energy, and tempo.

This project uses a simplified content-based approach. Each song stores its title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness. The user profile stores a favorite genre, favorite mood, target energy level, and acoustic preference. The current scoring system uses only genre, mood, and energy.

The scoring rules are:

- A matching mood adds 2.0 points.
- A matching genre adds 1.0 point.
- Energy adds up to 1.0 point based on how close the song's energy is to the user's target.

Mood receives the highest weight because the recommender is designed to support exploration across genres. A song from an unfamiliar genre can still rank highly when its mood and energy match the user's current preferences.

The system scores every song, sorts the results from highest to lowest, and returns the top recommendations. Tempo, valence, danceability, acousticness, and acoustic preference are stored but are not currently included in the scoring logic.

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

User profile: genre = J-Pop, mood = happy, energy = 0.75

```text
Top recommendations:

Matsuri - Score: 3.97/4.00
Because: Mood match (+2.0); Genre match (+1.0); Energy similarity (+0.97)

Rooftop Lights - Score: 2.99/4.00
Because: Mood match (+2.0); Genre mismatch (+0.0); Energy similarity (+0.99)

Sunrise City - Score: 2.93/4.00
Because: Mood match (+2.0); Genre mismatch (+0.0); Energy similarity (+0.93)

golden hour - Score: 2.80/4.00
Because: Mood match (+2.0); Genre mismatch (+0.0); Energy similarity (+0.80)

Mori no chiisana Restaurant - Score: 1.57/4.00
Because: Mood mismatch (+0.0); Genre match (+1.0); Energy similarity (+0.57)
```

---

## Experiments You Tried

I temporarily reduced the mood-match weight from 2.0 to 1.0, making mood and genre equally weighted.
- The Happy J-Pop and Focused Lofi profiles kept the same top songs because those songs matched both mood and genre.
- For the Intense K-Pop profile, “Good Goodbye” moved from fourth to first because its genre and energy matches became more influential.
- For the Chill Pop profile, pop songs moved above chill songs, showing that the original 2.0 mood weight strongly favored mood matches.
- The experiment produced different rankings, but they were not always more accurate. I restored the 2.0 mood weight because the system is designed to prioritize mood and encourage exploration across genres.

---

## Limitations and Risks

- Mood weight may dominate genre preferences.
- Mood labels are subjective.
- Manually estimated song attributes may be approximate.

---

## Reflection

I learned that recommenders turn song attributes and user preferences into rankings by assigning importance to each feature. Even a simple weighted system can feel personalized, but its results depend heavily on the selected weights and dataset labels.

Bias can appear when some preferences receive more weight, some genres or moods have fewer examples, or subjective labels do not match a listener's interpretation. This project showed me that a system can calculate scores correctly while still producing recommendations that feel less relevant to some users.

*See the complete [Model Card](model_card.md) for detailed evaluation, limitations, and future improvements.*



