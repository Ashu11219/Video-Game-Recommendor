def recommendor(user_genres, df):
    recommendations = []

    for _, row in df.iterrows():
        game_genres = row["genre_set"]

        score = len(user_genres & game_genres)

        if score > 0:
            recommendations.append({
                "name": row["name"],
                "score": score,
                "owners": row["owners"],
                "image": row["image"],
                "about": row["about"]
            })

    recommendations = sorted(recommendations,
                             key = lambda x: (x["score"], x["owners"]),
                             reverse = True)

    return recommendations[:10]