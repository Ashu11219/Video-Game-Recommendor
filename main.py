import pandas as pd
from input_processing import process_input
from model import Recommendor

df = pd.read_csv("data/cleaned_steam_games.csv")

df["tags_set"] = df["tags_set"].apply(eval)

user_games = [
    input("Enter recently played game 1: "),
    input("Enter recently played game 2: "),
    input("Enter recently played game 3: ")
]

mood = input("Enter your mood: ")
user_tags, matched_games = process_input(user_games, mood, df)

model = Recommendor(df)
results = model.recommend(user_tags, matched_games)

print("Recommended Games")
print()

for game in results:
    print(f"Name: {game["name"]}")
    print(f"Image URL: {game["image"]}")
    print(f"About: {game["about"][:150]}...")
    print()
