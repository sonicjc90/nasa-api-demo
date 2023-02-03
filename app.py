from flask import Flask, render_template
import requests
from datetime import date

app = Flask(__name__)

@app.route('/')
def index():
    today = str(date.today())
    response = requests.get("https://api.nasa.gov/planetary/apod?api_key=v5c19WhzIBKZKwuTc0LHo7fX8TSl81hddkCGyXNz&date="+today)
    data = response.json()

    return render_template('index.html' , data = data, date = today)

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')