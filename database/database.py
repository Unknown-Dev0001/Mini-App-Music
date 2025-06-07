from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)
db = client["flex_webmusic"]
song_collection = db["played_songs"]

async def save_song_play(user_id: int, user_name: str, song_title: str, duration: str):
    try:
        await song_collection.insert_one({
            "user_id": user_id,
            "user_name": user_name,
            "song_title": song_title,
            "duration": duration
        })
    except Exception as e:
        print(f"[DB Error] Failed to save song play: {e}")

async def get_user_song_history(user_id: int):
    try:
        return await song_collection.find({"user_id": user_id}).to_list(length=50)
    except Exception as e:
        print(f"[DB Error] Failed to retrieve history: {e}")
        return []