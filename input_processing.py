def process_input(user_games, mood, df):
    user_games = [g.lower().strip() for g in user_games]
    mood = mood.lower().strip()

    from rapidfuzz import process
    game_list = df["name"].tolist()
    matched_games = [process.extractOne(g, game_list)[0] for g in user_games]

    extracted_genres = df[df["name"].isin(matched_games)]
    genres = set()
    for g in extracted_genres["genre_set"]:
        genres.update(g)

    mood_map = {
    "chill": ["casual", "simulation"],
    "relaxed": ["casual", "indie"],
    "competitive": ["action", "sports"],
    "tryhard": ["action", "strategy"],
    "story": ["rpg", "adventure"],
    "immersive": ["rpg", "adventure"],
    "explore": ["adventure", "simulation"],
    "creative": ["simulation", "indie"],
    "fast": ["action", "racing"],
    "intense": ["action"],
    "strategy": ["strategy"],
    "multiplayer": ["massively multiplayer", "action"],
    "social": ["casual", "massively multiplayer"],
    "grindy": ["rpg", "massively multiplayer"],
    "fun": ["casual", "indie"],
    "short": ["casual", "indie"]
    }

    matched_mood = process.extractOne(mood, mood_map.keys())[0]
    if matched_mood in mood_map:
        genres.update(mood_map[matched_mood])

    return genres
