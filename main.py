from fastapi import FastAPI


app = FastAPI()


@app.get("/bot_home")
def bot_home():
    return {
        "message": "Who's your BotFather now!"
    }