from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from input_processing import process_input
from model import Recommendor

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi import Form
from fastapi.staticfiles import StaticFiles


app = FastAPI()
templates = Jinja2Templates(directory= "templates")
app.mount("/static", StaticFiles(directory= "static"), name = "static")
class UserInput(BaseModel):
    game1: str
    game2: str
    game3: str
    mood: str


df = pd.read_csv("data/cleaned_steam_games.csv")
df["tags_set"] = df["tags_set"].apply(eval)
model = Recommendor(df)

@app.get("/", response_class = HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html")
@app.post("/recommend-ui", response_class = HTMLResponse)
def recommend(
        request: Request,
        game1: str = Form(),
        game2: str = Form(),
        game3: str = Form(),
        mood: str = Form()

):
    user_games = [game1, game2, game3]

    user_tags, matched_games = process_input(user_games, mood, df)
    results = model.recommend(user_tags, matched_games)
    return templates.TemplateResponse(
        request,
    "index.html",
    {"results": results})
'''
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host = "0.0.0.0", port = 8000)'''