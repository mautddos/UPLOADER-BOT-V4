import os
from os import environ, getenv
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7685124406:AAHSlQuDOnmhiX5_jU4z1KZA5a3lbIe96aE")
    API_ID = int(os.environ.get("API_ID",22625636 ))
    API_HASH = os.environ.get("API_HASH", "f71778a6e1e102f33ccc4aee3b5cc697")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    MAX_FILE_SIZE = 2194304000
    TG_MAX_FILE_SIZE = 2194304000
    SESSION_STR = ""
    FREE_USER_MAX_FILE_SIZE = 2194304000
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    
    OUO_IO_API_KEY = ""
    MAX_MESSAGE_LENGTH = 4096
    PROCESS_MAX_TIMEOUT = 3600
    DEF_WATER_MARK_FILE = "@UploaderXNTBot"

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://zqffpg:1HKKatlqTOBcOwa6@cluster0.7dwrm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002536979045"))
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", "8167507955"))
    SESSION_NAME = "UploaderXNTBot"
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002536979045")

    TG_MIN_FILE_SIZE = 2194304000
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "urlmaut2bot")
    ADL_BOT_RQ = {}

    # Set False off else True
    TRUE_OR_FALSE = os.environ.get("TRUE_OR_FALSE", "").lower() == "false"

    # Shortlink settings
    SHORT_DOMAIN = environ.get("SHORT_DOMAIN", "")
    SHORT_API = environ.get("SHORT_API", "")

    # Verification video link
    VERIFICATION = os.environ.get("VERIFICATION", "")

    
