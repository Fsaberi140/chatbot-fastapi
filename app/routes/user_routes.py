from fastapi import FastAPI
from app.routes import chat_routes, user_routes

app = FastAPI

app.include_router(chat_routes.router , prefix='/chat' , tags=['chat'])
app.include_router(user_routes.router, prefix='/user', tags=['user'])

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Chatbot API"}


