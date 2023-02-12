from flask import Flask, request, render_template, jsonify
from voiceToText import controller


app = Flask(__name__,
            static_url_path='', 
            static_folder='static')


@app.route('/index', methods=['GET'])
def index():
    return app.send_static_file('index.html')

@app.route('/index1', methods=['GET'])
def index1():
    return app.send_static_file('index1.html')

@app.route('/index2', methods=['GET'])
def index2():
    return app.send_static_file('index2.html')

@app.route('/index3', methods=['GET'])
def index3():
    return app.send_static_file('index3.html')

@app.route('/index4', methods=['GET'])
def index4():
    return app.send_static_file('index4.html')

@app.route('/index5', methods=['GET'])
def index5():
    return app.send_static_file('index5.html')

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