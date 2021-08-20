from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def get_beer():
    res = requests.get('https://api.punkapi.com/v2/beers/random')
    beer_json = res.json()

    beer = {
        'name': beer_json[0]['name'],
        'first_brewed': beer_json[0]['first_brewed'],
        'description': beer_json[0]['description'],
        'foodpairing': beer_json[0]['food_pairing']
    }
    
    return render_template('index.html', beers=beer)

