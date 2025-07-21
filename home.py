#cd Users\Alex\UC\WeatherApp

from flask import Flask, render_template, redirect, url_for, request
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)


@app.get('/')
def home_get():
        return render_template('home.html', therm='--C°', place='')

@app.post('/')
def home_post():
     CITY = request.form.get('nm')
     return redirect(url_for('city_get', cty=CITY))
    


@app.get('/<cty>')
def city_get(cty):
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    load_dotenv()
    api_key = os.getenv('API_KEY')

    params = {
        'q': cty,
        'appid': api_key,
        'units': 'metric',
        'lang': 'en'
    }        

    response = requests.get(URL, params=params).json()
    temp = round(response['main']['temp'], 1)
    
    return render_template('home.html', therm=f'{temp}C°', place=cty)

@app.post('/<cty>')
def city_post(cty):
     CITY = request.form.get('nm')
     return redirect(url_for('city_get', cty=CITY))
     
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
