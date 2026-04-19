def recommendor(user_genres, user_games, df):
    recommendations = []

    for _, row in df.iterrows():
        game_tags = row["tags_set"]

        strong_tags = {
            "fps", "shooter", "action",
            "multiplayer", "pvp", "co-op",
            "open world", "story rich",
            "rpg", "survival"
        }
        medium_tags = {
            "adventure", "strategy", "tactical",
            "simulation", "sandbox", "exploration",
            "management", "crafting",
            "team-based", "real-time strategy",
            "turn-based"
        }
        score = 0
        for g in user_genres:
            if g in game_tags:
                if g in strong_tags:
                    score += 3
                elif g in medium_tags:
                    score += 2
                else:
                    score += 1

        popularity = row["owners"]
        reviews = row["positive"] + row["negative"]
        if reviews > 0:
            rating = row["positive"] / reviews
        else:
            rating = 0

        final_score = score * 5 + rating * 3 + (popularity / 1000000)

        if final_score > 0:
            if row["name"] in user_games:
                continue
            recommendations.append({
                "name": row["name"],
                "score": final_score,
                "owners": row["owners"],
                "image": row["image"],
                "about": row["about"]
            })

    recommendations = sorted(recommendations,
                             key = lambda x: (x["score"]),
                             reverse = True)

    return recommendations[:10]