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



