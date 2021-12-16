# import our main app from init
from app import app
# as well as import something from flask later
from flask import render_template


@app.route('/')
def home():
    players_list = ['Joao Cancelo', 'Fernandinho', 'Kevin De Bruyne', 'Phil Foden', 'Ruben Dias', 'John Stones', 'Ferran Torres']
    return render_template('index.html', players=players_list)