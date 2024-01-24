from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Bot(Base):
    __tablename__ = "bots"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String, unique=True, index=True)
    token = Column(String, unique=True, index=True)


