from pyrogram import filters
from pyrogram.types import Message
from client import app

@app.on_message(filters.command("start"))
async def start_command(_, message: Message):
    await message.reply(
        "👋 Welcome to **Flex Music WebApp Bot**!\n\n"
        "🎶 Use `/play <song name>` to search and stream songs directly in a beautiful WebApp music player!\n\n"
        "Example:\n`/play Until I Found You`"
    )