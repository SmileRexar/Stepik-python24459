import requests
import json

# eyt67259@zzrgg.com
from SimpleApi.basic_Controller.Weather import pretty_print_request

client_id = '2ed42f52ed8a8dc9bc7e'
client_secret = '6ec542deca8bc6b22bf46effd9ff2d83'

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
# создать заголовок содераи Header
headers = {"X-Xapp-Token": token}

with open('dataset_24476_4.txt', 'r', encoding='utf-8') as f:
    for line in f:
        # инииируем запрос с заголовком
        r = requests.get(f"https://api.artsy.net/api/artists/{line.strip()}", headers=headers)

        # разбор ответа сервера
        j = json.loads(r.text)
        print(j)
