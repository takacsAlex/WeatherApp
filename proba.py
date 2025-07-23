from dotenv import load_dotenv
import os
import requests

URL = 'https://api.openweathermap.org/data/2.5/weather'
load_dotenv()
api_key = os.getenv('API_KEY')

params = {
    'q' : 'Budapest',
    'appid' : api_key,
    'units' : 'metric',
    'lang' : 'en'
}

response = requests.get(URL, params=params).json()
temp = round(response['main']['temp'], 1)
desc = response['weather'][0]['description']
wind = round(response['wind']['speed'], 1)

print(response)
print()
print(desc)

