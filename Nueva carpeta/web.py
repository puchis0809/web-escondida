from flask import Flask

import random

 

app = Flask(__name__)

facts_list = ["as logradrado entrar bien tu premio es nada que esperabas "]

 

@app.route("/")

def index():

    return f'<h1>/Qué cosa es que corre mucho y no tiene pies</a>'

 

@app.route("/aire")

def facts():

    return f'<p>{random.choice(facts_list)}</p>'

 

app.run(debug=True)