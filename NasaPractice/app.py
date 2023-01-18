from flask import Flask, render_template, request
import requests
from datetime import date


#my api key? https://api.nasa.gov/planetary/apod?api_key=v5c19WhzIBKZKwuTc0LHo7fX8TSl81hddkCGyXNz 









app = Flask(__name__,template_folder="templates")


@app.route('/')

#def index():
    #return render_template('index.html')

#@app.route('/nasa')

def nasa():
    today=str(date.today())
    
    response = requests.get("https://api.nasa.gov/planetary/apod?api_key=v5c19WhzIBKZKwuTc0LHo7fX8TSl81hddkCGyXNz&date="+today)
    data= response.json()
    
    
    return render_template('nasa.html' , data=data)




if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')