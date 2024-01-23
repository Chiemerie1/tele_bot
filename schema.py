from pydantic import BaseModel



class CreateTeleBot(BaseModel):
    token: str
