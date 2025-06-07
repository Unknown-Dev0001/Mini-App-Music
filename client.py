from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

# Initialize Pyrogram client (bot mode)
app = Client(
    name="TGWebMusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=10,
    plugins=dict(root="plugins")
)