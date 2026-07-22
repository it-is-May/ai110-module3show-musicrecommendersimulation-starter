# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**AtmosMatch 1.0**

---

## 2. Intended Use  

- The recommender generates song suggestions based on a user's preferred genre, mood, and target energy.
- It is designed as a classroom prototype for exploring content-based recommendation systems.
- It assumes that a user can describe their current preferences using one genre, one mood, and one energy value.
- It is not intended to replace production music platforms that use large catalogs, listening history, and behavior from many users.  

---

## 3. How the Model Works  

- The recommender compares each song's mood, genre, and energy with the user's preferences.
- A mood match adds 2.0 points, and a genre match adds 1.0 point.
- Energy adds up to 1.0 point based on how close the song's energy is to the user's target.
- Mood has the highest weight because the system is designed to support exploration across genres.
- After scoring every song, the system sorts them from highest to lowest score and returns the top recommendations.
- Compared with the starter version, I implemented weighted scoring, case-insensitive matching, sorted results, and explanations for each scoring factor.
- Tempo, valence, danceability, acousticness, and acoustic preference are stored but are not currently used for scoring.

---

## 4. Data  

- The catalog contains 15 songs.
- Each song includes a title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness value.
- The dataset includes genres such as pop, J-Pop, K-Pop, and lofi, along with moods such as happy, chill, intense, focused, and whimsical.
- I expanded the starter catalog from 10 to 15 songs by adding five real songs.
- The dataset is small and uneven, so some genres and moods have more examples than others.
- It also does not represent listening history, multiple mood labels, or the full variety of musical taste.

---

## 5. Strengths  

- The recommender works well when a song matches both the user's preferred mood and genre.
- Energy similarity helps distinguish songs that otherwise receive similar mood and genre scores.
- Different user profiles produce noticeably different rankings.
- The scoring explanations clearly show how mood, genre, and energy affected each recommendation.
- The results are predictable because the same preferences and song data always produce the same ranking.
---

## 6. Limitations and Bias 

- **Ignored features:** The scoring function does not use tempo, valence, danceability, acousticness, or `likes_acoustic`.
- **Uneven representation:** The small dataset contains more examples of some genres and moods than others, so users who prefer less-represented categories may receive weaker recommendations.
- **Mood overfitting:** Mood contributes 2.0 points, while genre and energy each contribute at most 1.0 point.
- **Weight sensitivity:** Reducing the mood weight during the experiment caused genre-matching songs such as “Good Goodbye” to rank higher.
- **Exact-label matching:** Related labels such as “happy” and “whimsical” receive no partial match.
- **Subjective labeling:** Users whose interpretation differs from the dataset labels may receive less relevant recommendations.

---

## 7. Evaluation  

### Profiles Tested

I tested four user profiles:

- **Happy J-Pop:** Happy mood and moderately high energy.
- **Intense K-Pop:** Intense mood but lower energy.
- **Chill Pop:** Chill mood but high energy.
- **Focused Lofi:** Focused mood and low energy.

I checked whether songs matching each profile's mood, genre, and target energy appeared near the top. I also checked whether each profile returned five songs and whether scores were sorted from highest to lowest.

### Recommendation Outputs

```
================================================================================

Profile: Happy J-Pop
Preferences: genre=j-pop, mood=happy, energy=0.75

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

================================================================================

Profile: Intense K-Pop
Preferences: genre=k-pop, mood=intense, energy=0.4

Top recommendations:

Lose My Mind - Score: 2.57/4.00
Because: Mood match (+2.0); Genre mismatch (+0.0); Energy similarity (+0.57)

Storm Runner - Score: 2.49/4.00
Because: Mood match (+2.0); Genre mismatch (+0.0); Energy similarity (+0.49)

Gym Hero - Score: 2.47/4.00
Because: Mood match (+2.0); Genre mismatch (+0.0); Energy similarity (+0.47)

Good Goodbye - Score: 1.95/4.00
Because: Mood mismatch (+0.0); Genre match (+1.0); Energy similarity (+0.95)

Focus Flow - Score: 1.00/4.00
Because: Mood mismatch (+0.0); Genre mismatch (+0.0); Energy similarity (+1.00)

================================================================================

Profile: Chill Pop
Preferences: genre=pop, mood=chill, energy=0.85

Top recommendations:

Midnight Coding - Score: 2.57/4.00
Because: Mood match (+2.0); Genre mismatch (+0.0); Energy similarity (+0.57)

Library Rain - Score: 2.50/4.00
Because: Mood match (+2.0); Genre mismatch (+0.0); Energy similarity (+0.50)

Spacewalk Thoughts - Score: 2.43/4.00
Because: Mood match (+2.0); Genre mismatch (+0.0); Energy similarity (+0.43)

Sunrise City - Score: 1.97/4.00
Because: Mood mismatch (+0.0); Genre match (+1.0); Energy similarity (+0.97)

Gym Hero - Score: 1.92/4.00
Because: Mood mismatch (+0.0); Genre match (+1.0); Energy similarity (+0.92)

================================================================================

Profile: Focused Lofi
Preferences: genre=lofi, mood=focused, energy=0.35

Top recommendations:

Focus Flow - Score: 3.95/4.00
Because: Mood match (+2.0); Genre match (+1.0); Energy similarity (+0.95)

Library Rain - Score: 2.00/4.00
Because: Mood mismatch (+0.0); Genre match (+1.0); Energy similarity (+1.00)

Midnight Coding - Score: 1.93/4.00
Because: Mood mismatch (+0.0); Genre match (+1.0); Energy similarity (+0.93)

Coffee Shop Stories - Score: 0.98/4.00
Because: Mood mismatch (+0.0); Genre mismatch (+0.0); Energy similarity (+0.98)

Mori no chiisana Restaurant - Score: 0.97/4.00
Because: Mood mismatch (+0.0); Genre mismatch (+0.0); Energy similarity (+0.97)

================================================================================
```

### Surprising Result

“Matsuri” ranked first for the Happy J-Pop profile because it matched the preferred mood and genre, and its energy was close to the target. I expected “Mori no chiisana Restaurant” to rank higher, but its “whimsical” mood label did not exactly match “happy.” This showed that subjective labels can affect rankings.

### Profile Comparisons

- **Happy J-Pop vs. Intense K-Pop**: Happy J-Pop favored happy songs such as “Matsuri,” while Intense K-Pop favored intense songs such as “Lose My Mind.” This makes sense because mood has the highest scoring weight.
- **Happy J-Pop vs. Chill Pop**: Happy J-Pop returned upbeat songs, while Chill Pop returned chill songs such as “Midnight Coding.” Even though Chill Pop requested high energy, mood matches still ranked highest.
- **Happy J-Pop vs. Focused Lofi**: “Matsuri” ranked first for Happy J-Pop, while “Focus Flow” ranked first for Focused Lofi. Both songs matched their profile's mood and genre and were close to the target energy.
- **Intense K-Pop vs. Chill Pop**: Intense K-Pop ranked intense songs from other genres above K-Pop songs, while Chill Pop ranked chill songs from other genres above pop songs. Both results show that mood influences rankings more than genre.
- **Intense K-Pop vs. Focused Lofi**: The first Intense K-Pop result matched only the requested mood, while “Focus Flow” matched both mood and genre for Focused Lofi. This gave “Focus Flow” a higher score.
- **Chill Pop vs. Focused Lofi**: Both profiles returned some lofi songs, but for different reasons. Chill Pop favored them because of mood, while Focused Lofi favored them because of genre and low energy.

### Baseline Test Results

Before changing the mood weight, I ran the starter test suite and confirmed that both tests passed. Each profile also returned five songs sorted from highest to lowest score.

### Scoring Experiment

I temporarily reduced the mood-match weight from 2.0 points to 1.0 point, making mood and genre equally weighted. The Happy J-Pop and Focused Lofi profiles kept the same top recommendations because their first-ranked songs matched both mood and genre. However, “Good Goodbye” moved from fourth to first for Intense K-Pop, and pop songs moved above chill songs for Chill Pop. The experiment made genre more influential, but it was not automatically more accurate, so I restored the 2.0-point mood weight.

---

## 8. Future Work  

I would:
-  use more of the available song features, such as tempo, valence, danceability, and acousticness.
- support partial matches between related moods, such as “happy,” “whimsical,” and “energetic,” instead of requiring exact labels.
- add adjustable preference weights, a larger and more balanced catalog, and diversity rules for the top recommendations.
---

## 9. Personal Reflection  

I learned that simple scoring weights and dataset labels can strongly control recommendation results. I was surprised that a basic rule-based system could still produce recommendations that felt personalized. The project also showed me that a system can follow its logic correctly while still giving results that do not match a listener's interpretation. AI tools helped me review the scoring logic and plan experiments, but I verified the suggestions by reading the code, running tests, and comparing outputs. This changed how I view music apps because their recommendations depend heavily on how songs and user preferences are represented as data. If I extended the project, I would support related mood labels, adjustable feature weights, and a larger, more balanced song catalog.
