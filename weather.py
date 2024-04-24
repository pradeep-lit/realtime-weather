import requests
base_url='http://api.weatherapi.com/v1/current.json'
q=input("Enter the location : ")

param={
    'q':q,
    'key':'c2e533ad0eac4c59b9461917242404',
    'aqi':'yes'
}
data=requests.get(base_url,param)
djson=data.json()
print(f"Location : {djson['location']['name']}, {djson['location']['region']}, {djson['location']['country']}")
print(f"Temperature : {djson['current']['temp_c']}°C/{djson['current']['temp_f']}°F")
print(f"Feels like : {djson['current']['feelslike_c']}°C/{djson['current']['feelslike_f']}°F")
print(f"Condition : {djson['current']['condition']['text']}")
print(f"Wind : {djson['current']['wind_kph']}kmph")
print(f"Humidity : {djson['current']['humidity']}%")
print(f"UV index : {djson['current']['uv']}")
print(f"Pressure : {djson['current']['pressure_mb']} mBar")
print(f"Precipitation : {djson['current']['precip_mm']}mm")