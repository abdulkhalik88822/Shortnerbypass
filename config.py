# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "26641644"))
API_HASH = os.environ.get("API_HASH", "cc25b5e59e9d019b291b55719e1c6d09")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6007665412:AAE3pAX4ERHgQj5pA5HNNbTsCb5TiOjLxFg")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("6164919099")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Shbsnaubham")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Shubham:Shubhram89@cluster0.rqe6k2e.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "6164919099")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(6164919099)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001899231989")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "mdiskconvertorupdates") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
