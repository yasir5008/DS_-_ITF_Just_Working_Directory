from flask import Flask, request
import numpy as np
# import requests



app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world"

@app.route("/<name>")
def hello(name):
    # name="John"
    return f"Hello <b>{name.capitalize()}</b>, welcome to my homepage"



data = {
    "ankara":{"region":"middle anatolia", "pop":"3,5m","places":["ulus","kizilay","sincan"]},
    "izmir":{"region":"west anatolia", "pop":"4m","places":["kordon","saat kulesi","goztepe","konak"]},
    "konya":{"region":"middle anatolia","pop":"2m","places":["alaattin tepesi","mevlana turbesi"]}
        }

@app.route("/city/<city>")
def city(city):
    return {"data":str(data[city])}

@app.route("/city/<city>/<feature>")
def city_f(city,feature):
    return {"data":str(data[city][feature])}    

def mass_index(w,h):
    return h**2/w

@app.route("/calc")
def calc():
    w = int(request.args["w"])
    h = int(request.args["h"])
    return {"your mass index":f"{(mass_index(w,h)):.2f}"}   
    

def predict(vals):
    coefs = np.array([1,2,3])
    return sum(coefs*vals)




@app.route("/api", methods=["GET", "POST"])
def api():
    data = request.json.values()
    print(data)
    vals = [float(i) for i in data]
    print(vals)
    pred = predict(vals)
    print("result: ", pred)
    return {"prediction result":f"$ {pred:.2f}"}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)