# 🎮 Video Game Recommender System

A content-based video game recommender system that suggests games based on recently played titles and the user's current mood. Built using Python, Pandas, and intelligent input processing techniques like fuzzy matching and tag-based ranking.

---

## 🚀 Features

* 🔍 Fuzzy matching for real-world user inputs (e.g., "cod mw2")
* 🧠 Mood-based recommendation using tag mapping
* 🎯 Tag-weighted ranking system (strong / medium / weak features)
* 📊 Popularity-based sorting using estimated owners
* 🧹 Large dataset preprocessing (93K → optimized subset)
* ⚡ Fast CLI-based recommendations

---

## 🧠 How It Works

1. User inputs:

   * 3 recently played games
   * Current mood

2. System:

   * Matches game names using fuzzy matching
   * Extracts tags from matched games
   * Converts mood → relevant tags
   * Combines all tags into a user preference set

3. Model:

   * Compares user tags with each game’s tags
   * Assigns weighted scores
   * Sorts using:

     * Tag match score
     * Estimated owners (popularity)

4. Output:

   * Top 10 recommended games
   * Name, Image URL, Description

---

## 🛠️ Tech Stack

* Python
* Pandas
* RapidFuzz (for fuzzy matching)

---

## 📁 Project Structure

```
Video-Game-Recommendor/
│
├── data/
│   └── cleaned_steam_games.csv
│
├── preprocess.py
├── input_processing.py
├── model.py
├── main.py
└── README.md
```

---

## ⚠️ Challenges Faced (and Fixes)

### 1. Large Dataset (230MB) not pushing to GitHub

**Problem:** GitHub rejected files >100MB
**Fix:** Ignored raw dataset and only committed cleaned + reduced dataset

---

### 2. Git still tracking deleted large files

**Problem:** Old commits still contained large file
**Fix:** Reset local commits and recreated repo to remove history

---

### 3. Fuzzy Matching returning wrong games

**Problem:** Inputs like "cod" matched irrelevant entries
**Fix:** Added `score_cutoff` and manual alias mapping

---

### 4. Game name mismatch (COD MW2 ambiguity)

**Problem:** Multiple versions of same game
**Fix:** Introduced alias normalization before fuzzy matching

---

### 5. Poor recommendations using only genres

**Problem:** Genres too broad (e.g., "action")
**Fix:** Switched to tag-based filtering for higher precision

---

### 6. Random low-quality recommendations

**Problem:** No ranking beyond tag match
**Fix:** Added weighted scoring + popularity (owners)

---

### 7. Incorrect popularity sorting

**Problem:** Owners stored as ranges ("50000 - 100000")
**Fix:** Extracted max value using custom parsing function

---

### 8. Dataset encoding issues (weird characters)

**Problem:** Corrupted names like "Sekiroâ€¦"
**Fix:** Loaded CSV with proper encoding (`utf-8`)

---

### 9. Dataset too large for deployment

**Problem:** Cleaned dataset still >100MB
**Fix:** Reduced dataset to top ~50K games based on relevance

---

### 10. Mood mapping mismatch

**Problem:** Mood mapped to genres not present in dataset
**Fix:** Rebuilt mood map using actual dataset tags

---

### 11. Weak ranking quality

**Problem:** All tags treated equally
**Fix:** Introduced strong / medium / weak tag weighting

---

### 12. Already played games being recommended

**Problem:** Repetition in output
**Fix:** Filtered out user input games during recommendation

---
## 🧭 Project Workflow (Step-by-Step)

1. **Dataset Selection**

   * Chose Steam games dataset (~93K entries) from Kaggle.

2. **Initial Exploration**

   * Identified relevant columns: name, genres, tags, owners, about, image.

3. **Data Cleaning**

   * Removed null values.
   * Standardized text (lowercase, strip spaces).
   * Converted genres and tags into lists.
   * Parsed "owners" from range → numeric max value.

4. **Dataset Optimization**

   * Reduced dataset size (~93K → ~50K) to stay within GitHub limits and improve performance.

5. **Feature Engineering**

   * Created `genre_set` and `tags_set` for fast lookup.
   * Focus shifted from genres → tags for better precision.

6. **Input Processing Design**

   * Took 3 recently played games + mood as input.
   * Normalized user input (lowercase, trim).

7. **Fuzzy Matching**

   * Used RapidFuzz to match user input with dataset entries.
   * Added score cutoff to avoid incorrect matches.
   * Introduced alias handling (e.g., "cod" → "call of duty").

8. **Mood Mapping**

   * Mapped user mood → relevant tags (based on dataset tags, not assumptions).
   * Combined mood tags with extracted game tags.

9. **Scoring System Design**

   * Compared user tags with each game's tags.
   * Introduced weighted scoring:

     * Strong tags
     * Medium tags
     * Weak tags

10. **Ranking Logic**
    * Calculated final score using:
      * Tag match score (relevance)
      * Owners (popularity)
    * Sorted results in descending order.
11. **Filtering**
    * Removed already played games from recommendations.

12. **Output Formatting**

    * Returned top 10 games with:

      * Name
      * Image URL
      * Description

13. **Integration**

    * Connected:

      * `preprocess.py`
      * `input_processing.py`
      * `model.py`
      * `main.py`

14. **Testing & Iteration**

    * Tested with edge cases (e.g., "cod", partial names, different moods).
    * Refined fuzzy matching, scoring, and mood mapping multiple times.

15. **Final Optimization**

    * Balanced relevance vs popularity.
    * Ensured realistic and consistent recommendations.

16. **System Evolution**
    * Initial rule-based recommendation system lacked scalability, robustness, and real-world deployment feasibility.
    * To address this, the system was refactored using vectorized similarity techniques (TF-IDF + cosine similarity).
    * Restructured into a modular API-driven architecture using FastAPI, enabling efficient inference, cleaner separation of concerns, and production-ready deployment.
---
