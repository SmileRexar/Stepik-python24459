import requests
import json

client_id = '...'
client_secret = '...'

# инииируем запрос полуени токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбор ответа сервера
j = json.loads(r.text)

# токен
token = j["token"]
