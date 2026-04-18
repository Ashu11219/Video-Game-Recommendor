import pandas as pd

def extract_max(owners):
    try:
        return int(owners.split("-")[1].strip().replace(",", ""))
    except:
        return 0

df = pd.read_csv("data/steam_games.csv", encoding="utf-8", low_memory = False)

df = df[["Name", "Genres", "Estimated owners", "About the game", "Header image"]]
df.columns = ["name", "genres", "owners", "about", "image"]
df = df.dropna(subset = ["name", "genres"])
df["name"] = df["name"].str.lower().str.strip()
df["genres"] = df["genres"].apply(
    lambda x: [g.strip().lower() for g in x.split(",")]
)
df["owners"] = df["owners"].apply(extract_max)
df["about"] = df["about"].fillna("No description available. Please search on Steam.")
df = df.drop_duplicates(subset = ["name"])
df = df.reset_index(drop = True)
df["genre_set"] = df["genres"].apply(set)

df = df.sort_values(by = "owners", ascending = False).head(50000)
print(df[["name", "genres", "owners"]].head())
df.to_csv("data/cleaned_steam_games.csv", index = False)

