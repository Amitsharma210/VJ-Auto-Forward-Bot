from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "4f8f7336c4f9af5313a0933bc3c76fef")
      API_ID = int(getenv("API_ID", "25067764"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7332038790:AAGJY1oH9qIhJz3wdg7Bapuwjlg2q_io5LI")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002228700833:-1002212581572").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
