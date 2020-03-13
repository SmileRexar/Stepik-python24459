import requests
api = 'http://api.openweathermap.org/data/2.5/weather'

params= {
    'q':'moscow',
    'appid':'11c0d3dc6093f7442898ee49d2430d20'
}
res = requests.get(api, params=params)
print("\nStatus code: {0} "
      "\nContent-Type:{1}"
      "\nData.Json:{2}'".format(res.status_code, res.headers['Content-Type'], res.json()))
