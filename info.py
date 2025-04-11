from os import environ, getenv
import re
import os

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "5518489725"))
SILICON_PIC = os.environ.get("SILICON_PIC", "https://telegra.ph/file/21a8e96b45cd6ac4d3da6.jpg")
API_ID = int(getenv("API_ID", "28519661"))
API_HASH = str(getenv("API_HASH", "d47c74c8a596fd3048955b322304109d"))
BOT_TOKEN = str(getenv("BOT_TOKEN", ""))
FORCE_SUB = os.environ.get("FORCE_SUB", "-1002470391435") 
MONGO_DB = str(getenv("MONGO_DB", "mongodb+srv://spideyofficial777:6FwYFNcgrAPL8nqq@spidey777.pykfj.mongodb.net/?retryWrites=true&w=majority&appName=SPIDEY777",))
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b>File Name:- `{file_name}`\n\n{file_size}</b>",
    )
)
