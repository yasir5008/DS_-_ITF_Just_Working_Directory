from urllib import request
from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    return 'hello world'

@app.route("/<name>")
def hello(name):
    #name = 'jasons'
    return f"Hello <b>{name}</b>, welcome! to my website"
    
data ={
    "Ankara" :{"region": "middle-Anatolia", "population": "3,5", "place": ["ulus", "kizilay",'kecioren']},
    "Izmir" :{"region": "west-Anatolia", "population" : "3,5", "place": ["kordon","konak"]}
}

@app.route("/city/<city>")
def city(city):
    return {"data": str(data[city])}

def mass_indx(w,h):
    return h*h/w
    
@app.route("/calc")
def calc():
    w= float(request.args["w"])
    h=float(request.args["h"])
    return {"your mass index":f"{str(mass_indx(w,h)):.2f}"}


if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0',port=80)
