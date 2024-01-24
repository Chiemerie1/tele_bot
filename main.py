from fastapi import FastAPI, HTTPException, Depends
from schema import CreateTeleBot
import requests

from . import crud, models, schema
from .database import SessionLocal, engine
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)




app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/api/bot")
async def create_bot(create: CreateTeleBot):
    try:
        response = requests.get(f'https://api.telegram.org/bot{create.token}/getMe')
        data = response.json()
        if not response.status_code == 200 and data["ok"] == False:
            raise HTTPException(status_code=500, detail="Internal server error.")
        
        bot = models.Bot(
            id = data.data["id"],
            username = data.data["username"],
            first_name = data.data["first_name"],
            token=create.token

        )
        db.add(bot)
        

        return {
            "200 OK": "The bot is successfully created, and the token is obtained.",
            "data": data["result"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error.")


