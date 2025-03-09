from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

import json
import os
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()

API_KEY = os.getenv("API_KEY_IMPORT")

# Fear and greed
url = 'https://pro-api.coinmarketcap.com/v3/fear-and-greed/historical'

parameters = {
  'start':'1',
  'limit':'500',
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': API_KEY,
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  with open("./Data/fear-and-greed.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
  