#!/bin/python

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def index():
    #return render_template('teste.html')
    return "Hello World!"

app.run(host='0.0.0.0', port=8080) #host define o endereço IP e port define a porta utilizada. Escolhi 8080 para evitar conflitos.