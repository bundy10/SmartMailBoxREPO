from crypt import methods
import json
from tkinter import SW
from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import led
from led import LED, Switch, States

app = Flask(__name__)
cors = CORS(app)

@app.route('/', methods=['POST'])
def main():
    
    action = request.values['action']

    led = LED(3)

    if action == 'on':
        led.off()

    if action == 'off':
        States.state1()
        
    if action == 'accept':
        States.state2()

    return 'success'

@app.route('/switch', methods=['GET'])
def button():

    button = Switch(8)
    switchStatus = str(button.isTriggered())


    return switchStatus

