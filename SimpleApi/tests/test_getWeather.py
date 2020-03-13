from SimpleApi.basic_Controller.Weather import WeatherCheaker

#Sity = input("Input your sity:")
Sity='Moscow'
res = WeatherCheaker(Sity)
res_data = res.json()

def test_status_code_is_200():
    assert res.status_code==200
