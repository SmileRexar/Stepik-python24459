import requests
import json

#Disable debug information for request
debug_mode=False

def WeatherCheaker(city):
    api = 'http://api.openweathermap.org/data/2.5/weather'
    with open('Data_openWeather.json', 'r') as f:
        request_json = json.loads(f.read())

    # params= {
    #     'q':Sity,
    #     'appid':'11c0d3dc6093f7442898ee49d2430d20',
    #     'units':'metric'
    # }
    request_json['q'] = city

    res = requests.get(api, request_json)

    if debug_mode:
        pretty_print_request(res.request)

    print(f"\nStatus code: {res.status_code} "
          f"\nContent-Type:{res.headers['Content-Type']}"
          "\nRaw data json:{0}'".format(res.json()))
    return res

def pretty_print_request(request):
    print( '\n{}\n{}\n\n{}\n\n{}\n'.format(
        '-----------Request----------->',
        request.method + ' ' + request.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in request.headers.items()),
        request.body)
    )
def pretty_print_response(response):
    print('\n{}\n{}\n\n{}\n\n{}\n'.format(
        '<-----------Response-----------',
        'Status code:' + str(response.status_code),
        '\n'.join('{}: {}'.format(k, v) for k, v in response.headers.items()),
        response.text)
    )

if __name__=='__main__':
    Sity = input("Input your sity:")
    res=WeatherCheaker(Sity)
    res_data=res.json()
    print(f"Current temperature in {Sity} is {res_data['main']['temp']} C")
'''
    Example Json structure from service openweathermap
    {
        "coord": {
            "lon": xx.xx,
            "lat": xx.xx
        },
        "weather": [
            {
                "id": xxx,
                "main": "Clouds",
                "description": "broken clouds",
                "icon": "04n"
            }
        ],
        "base": "stations",
        "main": {
            "temp": xx.xx,
            "feels_like": xx.xx,
            "temp_min": xx.xx,
            "temp_max": xx.xx,
            "pressure": xx,
            "humidity": xx
        },
        "visibility": xx,
        "wind": {
            "speed": xx,
            "deg": xx
        },
        "clouds": {
            "all": xx
        },
        "dt": xx,
        "sys": {
            "type": 1,
            "id": xx,
            "country": "RU",
            "sunrise": xx,
            "sunset": xx
        },
        "timezone": xx,
        "id": xx,
        "name": "Moscow",
        "cod": 200
    }
    '''