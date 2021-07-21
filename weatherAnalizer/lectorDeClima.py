import requests
import json
def obtenerClima(ciudad):
  url = "https://api.openweathermap.org/data/2.5/weather"
  params = {"q": ciudad, "units": "metric",
            "appid": "d91d82974d11d89b31539399fa09e168"}
  response = requests.get(url, params=params)
  jsonDataString = response.text
  jsonDictionary = json.loads(jsonDataString)
  return jsonDictionary
  #print(json.dumps(jsonDictionary, indent=4, sort_keys=True))
