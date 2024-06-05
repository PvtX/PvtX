import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID","6435225"))
API_HASH = getenv("API_HASH","4e984ea35f854762dcde906dce426c2d")
BOT_TOKEN = getenv("BOT_TOKEN","5963562690:AAFjx6u04YmzTvJAgBbCpDnyYo3RDYEvV3U")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://aloneop90021:Alone3536@cluster0.480tfna.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "9999"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1001603822916"))
BOTADDLOGS = int(getenv("BOTADDLOGS", "-1001775986475")) # LOGGER_ID Id Also Use No Problem
GBAN_LOGS = int(getenv("GBAN_LOGS", "-1001775986475"))
GCAST_USERS = list(map(int, getenv("GCAST_USERS", "6079943111").split()))
OWNER_ID = int(getenv("OWNER_ID", 6079943111))
OWNER = int(getenv("OWNER", 6079943111))
OWNER_USERNAME = getenv("OWNER_USERNAME","ALONE_WAS_BOT")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/AloneXBot/AloneXAzure")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", "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")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AloneXBots")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/AlonesHeaven")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "400"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", 7000))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", 7000))
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "9999")) 
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))
STRING1 = getenv("STRING_SESSION", "BQEMf1sAjEIejS5eo-2THQgAIknYKox0bMIhv7-_T9Aw2TTuIBmpb2iZA5CLHkH6BnvC9iEpD8Kt54P6MZHrKK26JncVhnJENBceDHbweoSghiK5wgAuvR11rXG3_p6cvHfje8YBoIvLxn24EUsOtAXGGuwyzEhnHKYOts0rKITb-tm9a6K_Ray93Q_enJSL0LnV84FxOTDdhCUFxdEgCpgy2SYJyyHmoYhQIp4lvc5Q1d-Sai89jbvy5kRPwh85TfH1YYJuWs5Xjq3xOB3GQq3b-CE5BZOFM6ir7WPvWPDN1RvKNXFE8Mcn-8682mCyhEiRqKSUrBCqBvcQ2rpHrvQT-Nsx9gAAAAF2AZtFAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
AMBOT = [
    "💥",
    "⚡️",
    "💫",
]

START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/685709ad093730507337a.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://te.legra.ph/file/685709ad093730507337a.jpg")
PLAYLIST_IMG_URL = "https://te.legra.ph/file/685709ad093730507337a.jpg"
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://te.legra.ph/file/685709ad093730507337a.jpg")
TELEGRAM_AUDIO_URL = "https:/https://te.legra.ph/file/685709ad093730507337a.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/685709ad093730507337a.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/685709ad093730507337a.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/685709ad093730507337a.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/685709ad093730507337a.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/685709ad093730507337a.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/685709ad093730507337a.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/685709ad093730507337a.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
