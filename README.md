# 🎮 Find Your Next Obsession

A production-ready, ML-powered video game recommender system that suggests personalized games based on recently played titles and user mood — now deployed as a full-stack web application using FastAPI.

---

## 🚀 Features

- 🔍 Fuzzy matching for real-world inputs (e.g., "cod mw2")
- 🧠 Mood-based recommendation using intelligent tag mapping
- 🎯 Weighted scoring (strong / medium / weak tags)
- 📊 Popularity-aware ranking using owners data
- ⚡ TF-IDF + cosine similarity for improved relevance
- 🌐 FastAPI-powered backend API
- 🎨 Modern responsive UI (glassmorphism + grid layout)
- ⏳ Loading animation for real-world deployment latency

---

## 🧠 How It Works

1. User inputs:
   - 3 recently played games  
   - Current mood  

2. Input Processing:
   - Fuzzy matches game names  
   - Applies alias normalization  
   - Extracts tags from matched games  

3. Feature Engineering:
   - Mood → mapped to dataset-relevant tags  
   - Combined into a unified preference vector  

4. Model:
   - TF-IDF vectorization of game tags  
   - Cosine similarity to measure relevance  
   - Weighted scoring + popularity boost  

5. Output:
   - Top recommendations  
   - Game name, image, description  

---

## 🛠️ Tech Stack

- Python  
- Pandas  
- Scikit-learn (TF-IDF, cosine similarity)  
- RapidFuzz  
- FastAPI  
- Jinja2 (templating)  
- HTML/CSS (custom UI)  

---

## 📁 Project Structure

```
Video-Game-Recommendor/
│
├── data/
│   └── cleaned_steam_games.csv
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── preprocess.py
├── input_processing.py
├── model.py
├── main.py
├── requirements.txt
└── README.md
```

---
## ⚙️ Pre-Deployment Setup

### 1. FastAPI Integration

Converted the CLI-based system into a FastAPI application to enable real-world usage and deployment.

---

### 2. Why Pydantic?

Pydantic is used for:
- Input validation  
- Structured request handling  
- Preventing malformed API requests  

---

### 3. Running with Uvicorn

Uvicorn is the ASGI server used to run FastAPI apps.

Used for:
- Local testing  
- Debugging endpoints  
- Simulating production environment  

```bash
uvicorn app:app --reload
```

## ⚠️ Challenges Faced (and Fixes)

### 1. Fuzzy Matching Errors
**Problem:** Inputs like "cod" matched irrelevant games

**Fix:** Added score cutoff + alias mapping

---

### 2. Game Name Ambiguity

**Problem:** Multiple versions of same game

**Fix:** Normalized aliases before matching

---

### 3. Weak Genre-Based Recommendations

**Problem:** Genres too broad

**Fix:** Switched to tag-based system

---

### 4. Poor Ranking Quality

**Problem:** No differentiation in results

**Fix:** Added weighted scoring + popularity

---

### 5. Owners Stored as Ranges

**Problem:** Could not sort properly

**Fix:** Extracted max value for ranking

---

### 6. Dataset Encoding Issues

**Problem:** Corrupted names like "Sekiroâ€¦"

**Fix:** Loaded CSV with proper encoding (`utf-8`)

---

### 7. Mood Mapping Mismatch

**Problem:** Mood mapped to invalid tags

**Fix:** Rebuilt mapping using dataset tags

---

### 8. Repetition in Recommendations

**Problem:** Input games appearing again

**Fix:** Explicit filtering

---

### 9. TF-IDF Integration Complexity

**Problem:** Transition from rule-based → ML model

**Fix:** Modularized vector pipeline

---

### 10. FastAPI Template Errors
**Problem:** TemplateResponse breaking due to version changes

**Fix:** Updated to new signature

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
    * Started as CLI-based recommender
    * Improved with tag-weighted scoring
    * Upgraded using TF-IDF + cosine similarity
    * Converted into FastAPI backend
    * Integrated frontend UI
    * Prepared for cloud deployment
---

## 🚀 Deployment Notes
- Compatible with Render / Azure
- Uses Uvicorn as ASGI server
- Handles cold-start environments
- Fully API-driven architecture

---

## 💡 Key Takeaway
This project demonstrates:

```bash 
Rule-based logic → Machine Learning → API → Full Web Application
```

---

## 💡 Final Note
This is a complete system combining:

- Machine Learning
- Backend Engineering
- Frontend Development
- Deployment Readiness