import requests
api = 'http://api.openweathermap.org/data/2.5/weather'

params= {
    'q':'moscow',
    'appid':'11c0d3dc6093f7442898ee49d2430d20'
}
res = requests.get(api, params=params)
print(f"\nStatus code: {res.status_code} "
      f"\nContent-Type:{res.headers['Content-Type']}"
      "\nData.Json:{0}'".format(res.json()))


