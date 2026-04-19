from sklearn.feature_extraction.text import TfidfVectorizer as vec
from sklearn.metrics.pairwise import cosine_similarity as cs
import math

class Recommendor:
    def __init__(self, df):
        self.vectorizer = vec(max_features= 5000)
        feature_text = df["tags_set"].apply(lambda x: " ".join(x))
        self.game_vectors = self.vectorizer.fit_transform(feature_text)
        self.df = df

    def recommend(self, user_tags, user_games):
        user_text = " ".join(user_tags)
        user_vector = self.vectorizer.transform([user_text])

        similarities = cs(user_vector, self.game_vectors).flatten()
        recommendations = []

        for idx, row in self.df.iterrows():
            similarity_score = similarities[idx]

            popularity = math.log1p(row["owners"])
            reviews = row["positive"] + row["negative"]
            if reviews > 0:
                rating = row["positive"] / reviews
            else:
                rating = 0

            final_score = similarity_score * 10 + rating * 3 + popularity

            if final_score > 0:
                if row["name"] in user_games:
                    continue

                if similarity_score < 0.1:
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