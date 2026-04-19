from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from input_processing import process_input
from model import Recommendor

app = FastAPI()
class UserInput(BaseModel):
    game1: str
    game2: str
    game3: str
    mood: str


df = pd.read_csv("data/cleaned_steam_games.csv")
df["tags_set"] = df["tags_set"].apply(eval)
model = Recommendor(df)

@app.get("/")
def home():
    return {"message": "Game Recommender API is running"}
@app.post("/recommend")
def recommend(input: UserInput):
    user_games = [input.game1, input.game2, input.game3]

    user_tags, matched_games = process_input(user_games, input.mood, df)
    results = model.recommend(user_tags, matched_games)

    return results

print("Recommended Games")
print()

