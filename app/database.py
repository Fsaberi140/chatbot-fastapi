from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = 'mongodb://localhost:27017/chatbot'
client = AsyncIOMotorClient(MONGO_URI)
db = client.chatbot_db