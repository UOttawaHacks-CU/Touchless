import time
from flask import Flask, request, render_template, jsonify
import sys
from voiceToText import controller


app = Flask(__name__,
            static_url_path='', 
            static_folder='static')


@app.route('/index', methods=['GET'])
def index():
    return app.send_static_file('index.html')


@app.route('/form', methods=['GET'])
def form():
    # print("In controller")
    try:
        # print('In form route')
        result_text = controller()
        # print('After controller')
    except:
        return jsonify(result='ERROR : 400, bad request')

    return jsonify(result=result_text)