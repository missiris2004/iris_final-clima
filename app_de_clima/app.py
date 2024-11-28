from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather_data(city: str):
    API_KEY = '48c114e3cf3b98f1361991428eff9760'
    idioma = 'es'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang={idioma}&appid={API_KEY}'
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

@app.route("/cv")
def cv():
    return render_template("cv.html")


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            data = get_weather_data(city)
            if data and data.get('cod') == 200:
                return render_template('iris.html', data=data)
            return render_template('iris.html', error="Ciudad no encontrada")
    return render_template('iris.html')

if __name__ == "__main__":
    app.run(debug=True)
