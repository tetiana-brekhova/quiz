import requests


parameters = {"amount": 50,
              "type": "boolean"}

API = "https://opentdb.com/api.php"

data = requests.get(url=API, params=parameters).json()
question_data = data["results"]