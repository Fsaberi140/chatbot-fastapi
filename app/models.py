from pydantic import BaseModel, EmailStr
from typing import Optional


class User(BaseModel):
    username: str
    password: str
    email: EmailStr

class Message(BaseModel):
    sender: str
    receiver: str
    message: str
    timestamp: Optional[str]= None