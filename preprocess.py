import pandas as pd

def extract_max(owners):
    try:
        return int(owners.split("-")[1].strip().replace(",", ""))
    except:
        return 0

df = pd.read_csv("data/steam_games.csv", encoding="utf-8", low_memory = False)

df = df[["Name", "Tags", "Estimated owners", "About the game", "Header image", "Metacritic score", "Positive", "Negative"]]
df.columns = ["name", "tags", "owners", "about", "image", "metacritic", "positive", "negative"]
df = df.dropna(subset = ["name", "tags"])
df["name"] = df["name"].str.lower().str.strip()
df["tags"] = df["tags"].apply(
    lambda x: [g.strip().lower() for g in x.split(",")]
)
df["owners"] = df["owners"].apply(extract_max)
df["about"] = df["about"].fillna("No description available. Please search on Steam.")
df = df.drop_duplicates(subset = ["name"])
df = df.reset_index(drop = True)
df["tags_set"] = df["tags"].apply(set)
df["feature_text"] = df["tags"].apply(lambda x: " ".join(x))

df = df.sort_values(by = "owners", ascending = False).head(50000)

df.to_csv("data/cleaned_steam_games.csv", index = False)

