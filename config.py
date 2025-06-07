import os

# Telegram Bot Credentials
API_ID = int(os.getenv("API_ID", "YOUR_API_ID"))
API_HASH = os.getenv("API_HASH", "YOUR_API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN")

# MongoDB URI
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://your_mongo_uri")

# Logging Group (for logs)
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "-1001234567890"))

# Mini App Base URL (e.g., Render or Vercel deployed web app)
MINI_APP_URL = os.getenv("MINI_APP_URL", "https://yourdomain.com")

# Fallback thumbnail
YT_THUMBNAIL = os.getenv("YT_THUMBNAIL", "https://telegra.ph/file/3c5e0b1f7ec86bb34d81f.jpg")