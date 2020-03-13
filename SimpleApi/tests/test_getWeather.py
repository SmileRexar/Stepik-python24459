from SimpleApi.basic_Controller import Weather
from SimpleApi.basic_Controller.Weather import *

#Sity = input("Input your sity:")

Sity='Moscow'

Weather.debug_mode=True
res = WeatherCheaker(Sity)
res_data = res.json()

pretty_print_response(res)

def test_status_code_is_200():
    assert res.status_code==200
