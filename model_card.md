# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeMatch 1.0**

A simple music recommender that matches songs to a listener's taste.

---

## 2. Intended Use

This model recommends songs to a listener based on their taste.

The listener gives three things: a favorite genre, a favorite mood, and a
target energy level. The model then picks the 5 songs that fit best.

It assumes the listener knows what they like and can describe it with those
three simple choices. It also assumes taste can be captured by genre, mood,
and energy alone, which is not fully true in real life.

This is a classroom project for learning, not a real product. It runs on a
tiny made-up song list, so it is meant for exploring how recommenders work,
not for real listeners.

---

## 3. How the Model Works

Each song has a genre, a mood, and an energy level. The listener gives their
favorite genre, favorite mood, and a target energy level.

The model gives every song a score. It works like earning points:

- If the song's genre matches, it earns points.
- If the song's mood matches, it earns some points too.
- For energy, the closer the song is to the target, the more points it gets.

A genre match is the strongest signal, so it is worth the most. Mood is next.
Energy adds points based on how close it is, so a song does not have to be a
perfect match to still do well.

Once every song has a score, the model sorts them from highest to lowest and
shows the top 5. It also lists the reasons each song scored well, so you can
see why it was picked.

The starter code was empty, with the main parts left to build. I wrote the
part that reads the song list from a file, the part that scores one song, and
the part that ranks all the songs and returns the best ones. I also tried
changing the weights (for example making energy count twice as much) to see
how the results would change.

---

## 4. Data

The catalog has 18 songs. Each song has a title, artist, genre, mood, energy,
tempo, valence, danceability, and acousticness.

It covers 15 genres, including pop, lofi, rock, ambient, jazz, synthwave,
hip hop, classical, electronic, country, reggae, metal, r&b, and folk. The
moods range from happy and chill to intense, sad, and aggressive.

The starter file had 10 songs. I added 8 more to cover more genres and moods,
so the model would have more variety to work with.

A lot of real musical taste is still missing. There are no lyrics, no
language, and no artist history. The list is also tiny and made up, so it does
not reflect what real people actually listen to. Many genres only have one
song, so there is not much depth.

---

## 5. Strengths

The model works best for listeners with a clear, mainstream taste. A pop fan
or a lofi fan gets a top 5 that really fits, because those genres have several
songs to choose from.

The scoring captures the big picture well. It reliably puts the best all-around
match at the top. For every profile I tested, the #1 song matched all three
preferences and scored near the maximum.

It also matched my intuition on the easy cases. The chill lofi listener got
calm, quiet songs, and the intense rock listener got loud, high-energy songs.

One nice thing is that it explains itself. Every recommendation comes with the
reasons it was picked, so it is easy to see why a song made the list.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 
The system has several weaknesses that surfaced during testing.

Prompts:  

- Features it does not consider  

The scorer uses only genre, mood, and energy. It ignores valence (musical happiness), danceability, acousticness, and tempo — all of which are in the dataset. Because of this it cannot tell a high-energy *happy* song from a high-energy *angry* one, so an upbeat-pop listener can be handed an aggressive track just because the energy number
matches.'

- Genres or moods that are underrepresented  

The catalog is heavily skewed:
lofi has 3 songs and pop has 2, but 13 of the 15 genres have only a single song each. A mainstream listener (e.g. Chill Lofi) gets a coherent top 5 of real matches, while the Deep Intense Rock profile gets exactly one true match (Storm Runner) followed by four unrelated songs that only share a similar energy level.

- Cases where the system overfits to one preference  

After my weight-shift experiment (energy weighted 2.0, genre 1.0), the system leaned so heavily on energy that a song matching *only* the user's energy level could nearly outrank a genuine genre-and-mood match. Overweighting any single feature causes the
recommendations to collapse onto that one dimension.


- Ways the scoring might unintentionally favor some users  

Because the ranker always returns k songs with no minimum relevance score, it fills empty slots with off-target "filler." This means the system serves well-represented,
mainstream-genre users far better than niche-genre users, and its quality depends more on how balanced the dataset is than on the scoring rules themselves. It also only does exact label matching, so it never connects similar styles (e.g. "indie pop" to "pop") — trapping users in a narrow filter bubble of the exact label they typed.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  

I tested the recommender with three very different listeners so I could see
whether the results changed in ways that made sense:

- **High-Energy Pop** — likes pop, happy mood, high energy (0.9)
- **Chill Lofi** — likes lofi, chill mood, low energy (0.4)
- **Deep Intense Rock** — likes rock, intense mood, high energy (0.9)

- What you looked for in the recommendations  

whether each profile's #1 pick was a song that truly fit all three preferences, and whether the rest of the list "felt right" for that kind of listener. I also ran a weight-shift experiment (making energy count twice as much) and tried some deliberately tricky profiles to see where the system breaks.

- What surprised you 

the top pick for every profile was a near-perfect match,
which was reassuring — but the *bottom* of each list was often filled with songs
that had nothing to do with the user's taste and only shared a similar energy
level. I was also surprised that doubling the importance of energy barely
changed the rankings; it mostly just changed the scores. This told me the small
size of the song catalog matters more than the exact scoring weights.

- Any simple tests or comparisons you ran  

**High-Energy Pop vs. Chill Lofi.** These two lists are almost complete
opposites, which is exactly what I'd hope for. The pop listener gets loud,
upbeat, high-energy songs (Sunrise City, Gym Hero), while the lofi listener gets
calm, quiet, low-energy songs (Midnight Coding, Library Rain). They barely share
any songs. This makes sense because they want opposite energy levels *and*
different genres, so almost nothing overlaps.

**High-Energy Pop vs. Deep Intense Rock.** These two are more interesting because
they *both* want high energy (0.9). As a result they share some of the same
loud songs (like Gym Hero and Neon Overdrive), but their #1 picks are different:
the pop fan gets Sunrise City (a happy pop song) and the rock fan gets Storm
Runner (an intense rock song). This shows the system correctly uses genre and
mood to separate two people who want the same *energy* but a different *style*.

**Chill Lofi vs. Deep Intense Rock.** Another near-opposite pair. Lofi gets
soft, low-energy tracks; rock gets loud, aggressive, high-energy tracks. There
is essentially no overlap, which makes sense — one wants calm background music
and the other wants intense, driving music. They sit at opposite ends of almost
every attribute.


# Why "Gym Hero" keeps showing up for "Happy Pop" listeners

Gym Hero is a pop song, but its mood is labeled *intense* (it's a workout
anthem), not *happy*. When a "Happy Pop" listener asks for recommendations, the
system gives Gym Hero points for two reasons: it's the right genre (pop), and
it's very high-energy (0.93), which is close to what the listener asked for
(0.9). So even though the song isn't actually "happy," it scores well and keeps
appearing near the top. The system doesn't understand that a pumped-up gym track
feels completely different from a cheerful, feel-good pop song — it only sees
"pop" and "high energy" and assumes that's a good match. This is a good example
of the system matching *numbers and labels* rather than the real *feeling* of
the music.

No need for numeric metrics unless you created some.

---

## 8. Future Work

There are a few things I would improve next.

- **Use more features.** I would add valence (how happy a song sounds) and
  danceability, so the model could tell a happy song from an angry one even
  when their energy is the same.
- **Add a quality cutoff.** Right now it always returns 5 songs, even weak
  ones. I would skip songs below a minimum score so it stops showing filler.
- **Understand similar styles.** I would let it know that "indie pop" is close
  to "pop," so it can suggest songs the listener did not ask for by name.
- **More variety in the top 5.** I would avoid filling the list with songs
  that all match on just one thing.
- **Handle mixed tastes.** I would let listeners pick more than one genre or
  mood, since real taste is rarely just one thing.
- **A bigger, real song list.** More songs, especially in the rare genres,
  would give better and fairer results.

---

## 9. Personal Reflection

I learned that a recommender is really just a scoring system. It turns taste
into numbers, adds up points, and sorts the results. There is no magic to it.

The most interesting thing I discovered was how much the choices behind the
scoring matter. The weights I picked and the songs in the list shaped the
results as much as the code did. I was surprised that changing the weights
barely moved the rankings, because the small song list mattered more.

This changed how I think about apps like Spotify. When they suggest a song, it
is based on rules and data that someone chose. If the data is uneven or a
feature is missing, the suggestions can quietly become biased, even when the
code is working exactly as intended.

### Reflection on my engineering process

**My biggest learning moment** was realizing that designing the scoring rule
was the real work, not the coding. Deciding how many points a genre match
should be worth compared to mood or energy shaped the whole system. The code
was the easy part. The thinking behind it was the hard part.

**AI tools helped me** move faster and understand ideas. They helped me
scaffold the functions, explain concepts like content-based filtering, and
format the output so it was easy to read. But I had to double-check them. When
I changed the weights, I ran the program and checked the results myself instead
of trusting that the change was an improvement. A few times the output looked
fine but did not match musical common sense, like an intense workout song being
suggested to a happy-pop listener. I had to test with real profiles and use my
own judgment to catch that.

**What surprised me** was how a few simple rules could still "feel" like real
recommendations. It is only adding up points and sorting a list, but the top 5
looked like something a person might actually put together. It made me see that
recommendations do not need to be complex to seem smart.

**What I would try next** is adding more song features like valence and
danceability, using a bigger and more balanced song list, and maybe mixing in
what similar listeners like (not just song attributes). I think that would make
the suggestions feel less repetitive and more personal.
