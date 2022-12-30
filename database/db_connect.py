import motor
import motor.motor_asyncio
from beanie import init_beanie

from models.book import Book
from models.user import User

async def init__db():
    client=motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/sample")

    await init_beanie(
        database=client.db_name,
        document_models=[Book,User]

    )