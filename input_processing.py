def process_input(user_games, mood, df):
    alias_map = {
        "cod": "call of duty",
        "mw": "modern warfare",
        "mw1": "modern warfare",
        "mw2": "modern warfare 2",
        "mw3": "modern warfare 3",
        "warzone": "call of duty warzone",

        "cs": "counter strike",
        "csgo": "counter strike global offensive",
        "valo": "valorant",
        "bf": "battlefield",
        "bf1": "battlefield 1",
        "bf5": "battlefield v",

        "gta": "grand theft auto",
        "gta5": "grand theft auto v",
        "gta v": "grand theft auto v",
        "rdr": "red dead redemption",
        "witcher": "the witcher",
        "witcher3": "the witcher 3",
        "skyrim": "elder scrolls v skyrim",
        "elden": "elden ring",
        "souls": "dark souls",

        "mc": "minecraft",
        "rl": "rocket league",
        "fn": "fortnite",
        "pubg": "playerunknown battlegrounds",
        "civ": "civilization",
    }

    def expand_alias(text):
        text = text.lower()

        for key in alias_map:
            if key in text:
                text = text.replace(key, alias_map[key])

        return text

    user_games = [expand_alias(g.lower().strip()) for g in user_games]
    mood = mood.lower().strip()

    from rapidfuzz import process
    game_list = df["name"].tolist()
    matched_games = []
    for g in user_games:
        match = process.extractOne(g, game_list, score_cutoff=70)

        if match:
            print(match)
            matched_games.append(match[0])

    extracted_tags = df[df["name"].isin(matched_games)]
    tags = set()
    for g in extracted_tags["tags_set"]:
        tags.update(g)

    mood_map = {
        "chill": ["casual", "relaxing", "simulation", "sandbox", "building"],
        "relaxed": ["casual", "indie", "pixel graphics", "2d"],
        "competitive": ["action", "fps", "shooter", "multiplayer", "pvp", "team-based"],
        "tryhard": ["fps", "shooter", "tactical", "competitive", "action"],
        "story": ["story rich", "adventure", "rpg", "singleplayer", "narrative"],
        "immersive": ["open world", "story rich", "rpg", "exploration"],
        "explore": ["open world", "exploration", "sandbox", "adventure"],
        "creative": ["sandbox", "building", "crafting", "simulation"],
        "fast": ["action", "fps", "shooter", "racing"],
        "intense": ["action", "fps", "shooter", "survival", "horror"],
        "strategy": ["strategy", "tactical", "management", "turn-based", "real-time strategy"],
        "multiplayer": ["multiplayer", "co-op", "online co-op", "team-based", "pvp"],
        "social": ["multiplayer", "co-op", "casual"],
        "grindy": ["rpg", "loot", "survival", "massively multiplayer"],
        "fun": ["casual", "funny", "party", "arcade"],
        "short": ["casual", "indie", "2d", "arcade"]
    }

    matched_mood = process.extractOne(mood, mood_map.keys())[0]
    if matched_mood in mood_map:
        tags.update(mood_map[matched_mood])

    return tags
