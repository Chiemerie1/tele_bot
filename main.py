from fastapi import FastAPI, HTTPException
from schema import CreateTeleBot
import requests


app = FastAPI()

bots = []

@app.get("/")
async def bot_home():
    return {
        "message": "Who's your BotFather now!"
    }


@app.post("/api/bot")
async def create_bot(create: CreateTeleBot):
    try:
        response = requests.get(f'https://api.telegram.org/bot{create.token}/getMe')
        data = response.json()
        if not response.status_code == 200 and data["ok"] == False:
            raise HTTPException(status_code=500, detail="Internal server error.")
        
        return {
            "200 OK": "The bot is successfully created, and the token is obtained."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error.")


