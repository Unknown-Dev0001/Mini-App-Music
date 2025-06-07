import os

# Telegram Bot Credentials
API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# MongoDB URI
MONGO_URL = os.getenv("MONGO_URL", "")

# Logging Group (for logs)
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", -1002078575375))

# Mini App Base URL (e.g., Render or Vercel deployed web app)
MINI_APP_URL = os.getenv("MINI_APP_URL", "")

# Fallback thumbnail
YT_THUMBNAIL = os.getenv("YT_THUMBNAIL", "https://i.ibb.co/Q3J5VnZq/Img2url-bot.jpg")