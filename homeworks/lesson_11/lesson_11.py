import requests

GIPHY_URL = "http://api.giphy.com/v1/gifs/search"
API_KEY = "KrKw4ryAGkaH3bO0J63TnkpTp46PyV7C"
search_input = "cat"

req = requests.get(
    GIPHY_URL,
    params={
        "q": search_input,
        "api_key": API_KEY,
        "limit": "1"
      }
)

result = req.json()["data"][0]["url"]

print(result)

# TELEG_TOKEN = "6179781599:AAHi3O_MNuZdIK1cagZF7iqgzUSEspcTWmA"
# BOT_URL = "t.me/gif_proj_bot"

# TELEG_URL = "https://api.telegram.org/bot"


# import asyncio
# import telegram


# async def main():
#     bot = telegram.Bot(TELEG_TOKEN)
#     async with bot:
#         print((await bot.get_updates())[0])

