#cd UC/WeatherApp

from flask import Flask, render_template, redirect, url_for, request
import requests

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST': 
        CITY = request.form['nm']
        return redirect(url_for('city', cty=CITY))
    else:
        return render_template('home.html', homero='--C°', varos=CITY)
        
@app.route('/<cty>', methods=['GET', 'POST'])
def city(cty):
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    API_KEY = 'c5e9dd8bafe6a531746296d2fa76d36e'  

    params = {
        'q': cty,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'en'
    }        

    response = requests.get(URL, params=params).json()
    # print(response)
    temp = round(response['main']['temp'], 1)
    # print(temp)
    
    if request.method == 'POST': 
        CITY = request.form['nm']
        return redirect(url_for('city', cty=CITY))
    else:
        return render_template('home.html', homero=temp, varos=cty)
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
