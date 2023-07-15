from flask import Flask
import random

coin_sides = ['Орёл', 'Решка']

app = Flask(__name__)

@app.route("/random_side")
def coin_random():
    return f'<p>{random.choice(coin_sides)}</p>'

app.run(debug=True)