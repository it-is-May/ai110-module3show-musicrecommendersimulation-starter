# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

In real-world music platforms, recommendation systems may use collaborative filtering, content-based filtering, or both. Collaborative filtering uses behavior from many users, such as likes, skips, playlists, and listening history. Content-based filtering compares a user's preferences with song attributes such as genre, mood, energy, and tempo.

This project uses a simplified content-based approach. Each song stores information such as its title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness. The user profile stores a favorite genre, favorite mood, target energy level, and acoustic preference. This first version uses only genre, mood, and energy when calculating scores.

The first version of the scoring system prioritizes three features:

- A matching mood adds 2.0 points.
- A matching genre adds 1.0 point.
- Energy receives a similarity score based on how close the song's energy is to the user's target energy.

Mood receives the highest weight because this recommender is designed to support exploration across genres. A song from an unfamiliar genre can still rank highly when its mood and energy match the user's current preference.

The system calculates a score for every song, sorts the songs from highest to lowest score, and returns the top recommendations. Additional song attributes, including tempo, valence, danceability, and acousticness, remain in the dataset but are not included in the first version of the scoring logic. Acoustic preference is also stored in the user profile but is not currently used for scoring.

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

User profile: genre=j-pop, mood=happy, energy=0.75

```text
Top recommendations:

Matsuri - Score: 3.97/4.00
Because: Mood match (+2.0); Genre match (+1.0); Energy similarity (+0.97)

Rooftop Lights - Score: 2.99/4.00
Because: Mood match (+2.0); Energy similarity (+0.99)

Sunrise City - Score: 2.93/4.00
Because: Mood match (+2.0); Energy similarity (+0.93)

golden hour - Score: 2.80/4.00
Because: Mood match (+2.0); Energy similarity (+0.80)

Mori no chiisana Restaurant - Score: 1.57/4.00
Because: Genre match (+1.0); Energy similarity (+0.57)
```

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Because mood has the highest scoring weight, songs with the preferred mood may rank above songs from the user's preferred genre. This supports exploration across genres, but it may work less well for users who consider genre more important than mood. Mood labels are also subjective and may not match every listener's interpretation.

Some real songs were manually labeled using listening impressions and publicly available music metadata. Subjective attributes such as mood, energy, danceability, and acousticness are approximate and may vary across listeners or analysis platforms.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



