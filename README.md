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

Explain your design in plain language.

This is a **content-based** music recommender. It scores each song by how well
its attributes match a user's stated preferences, then returns the best matches.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
  
- **genre** – category (pop, lofi, rock, …)
- **mood** – feel (chill, happy, intense, …)
- **energy** – how energetic the track is (0–1)

- What information does your `UserProfile` store

- **favorite_genre** – preferred genre
- **favorite_mood** – preferred mood
- **target_energy** – desired energy level (0–1)

- How does your `Recommender` compute a score for each song

Each song starts at **0** and earns points from three rules (max **4.0**):

| Rule | Points | Logic |
|------|--------|-------|
| Genre match | **+2.0** | `+2.0` if the song's genre equals the user's favorite genre |
| Mood match | **+1.0** | `+1.0` if the song's mood equals the user's favorite mood |
| Energy similarity | **0.0–1.0** | `1 - abs(target_energy - song_energy)` |

The energy rule rewards *closeness* to the target, not just high or low values,
so a song near the user's target energy scores higher than one at either extreme.

**Weighting rationale:** a genre match is worth twice a mood match because genre
sets the overall "lane," while mood and energy fine-tune within it. A perfect
energy match (1.0) can equal a mood match but can never outweigh a genre match.


- How do you choose which songs to recommend

1. **Score** every song in the catalog with the recipe above.
2. **Sort** all songs from highest score to lowest.
3. **Return the top `k`** (default 5), each with its score and reasons.

## Data flow
Input (user_prefs) → Process (loop: score every song) → Output (sort, take top K)

## Potential biases & limitations
- **Genre over-prioritization.** Because genre is worth 2.0 (double any other
  rule), the system can bury songs that perfectly match the user's *mood* and
  *energy* simply because they sit in a different genre — e.g. a chill ambient
  track ranked below a lofi track the user likes less well.
- **Label dependence over sound.** Genre and mood are exact-match only, so the
  system has no notion that lofi, ambient, and jazz are sonically similar. Two
  near-identical songs can score far apart just because their labels differ.
- **Narrow, self-reinforcing results (filter bubble).** Content-based scoring
  keeps recommending more of what the user already likes and rarely surfaces
  genuinely new styles (low serendipity).
- **Limited feature depth.** Only genre, mood, and energy drive the score;
  danceability, valence, acousticness, and tempo are ignored, so songs that
  differ meaningfully on those feel "identical" to the recommender.
- **Popularity/representation bias.** Genres with more songs in the catalog have
  more chances to match and rank, while sparsely represented genres (e.g. metal,
  classical) can only ever produce one or two candidates.


---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

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

Loaded songs: 18

============================================
  TOP RECOMMENDATIONS
  for a pop / happy listener (energy ~0.8)
============================================

1. Sunrise City - Neon Echo
   Score: 3.98 / 4.0
   Why:
     - genre match: pop (+2.0)
     - mood match: happy (+1.0)
     - energy 0.82 close to target 0.8 (+0.98)

2. Gym Hero - Max Pulse
   Score: 2.87 / 4.0
   Why:
     - genre match: pop (+2.0)
     - energy 0.93 close to target 0.8 (+0.87)

3. Rooftop Lights - Indigo Parade
   Score: 1.96 / 4.0
   Why:
     - mood match: happy (+1.0)
     - energy 0.76 close to target 0.8 (+0.96)

4. Concrete Dreams - Cipher Lane
   Score: 0.98 / 4.0
   Why:
     - energy 0.78 close to target 0.8 (+0.98)

5. Night Drive Loop - Neon Echo
   Score: 0.95 / 4.0
   Why:
     - energy 0.75 close to target 0.8 (+0.95)
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



