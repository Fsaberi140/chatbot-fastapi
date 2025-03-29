from typing import Optional
from pydantic import BaseModel, EmailStr


class UserCreateSchema(BaseModel):
    username: str
    password: str
    email: EmailStr

class ChatMessageSchema(BaseModel):
    sender: str
    receiver: str
    message: str
    timestamp: Optional[str]= None