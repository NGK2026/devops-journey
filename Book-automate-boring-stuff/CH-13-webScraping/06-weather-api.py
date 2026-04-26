import requests

city_name = 'Cairo'
country_code = 'EG'
API_key = '4e9973cafb72f0eb808a1e70c4511bce'
lat = 30.0443879
lon = 31.2357257
# lat = 30.10
# lon = 31.24
# response = requests.get(f'https://api.openweathermap.org/geo/1.0/direct?q={city_name}&{country_code}&appid={API_key}')


# response = requests.get(f'https://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&appid={API_key}')

# response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_key}')

response = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={API_key}')
print(response.text)
print()
import json
response_data = json.loads(response.text)
print(response_data)
print()
# print(response_data['main']['temp'])
print(response_data['list'][0]['main'])