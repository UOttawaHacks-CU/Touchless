# import time
# from flask import Flask, request, render_template, jsonify
# import sys

# sys.path.insert(1, '../gestures')
# from gestureRecognizer import collectGestures

# app = Flask(__name__)

# @app.route('/form', methods=['GET', 'POST'])
# def form():
#     # handle the POST request
#     if request.method == 'POST':
#         try:
#             body = request.get_json()
#             print(body)
#             text = body['text']
#             print(text)
#         except:
#             return jsonify(result='ERROR : 400, bad request')

#     return jsonify(result='ERROR : 404, only POST req allowed or service not available')


# # @app.route('/textToSpeech', mthods=['GET', 'POST'])
# # def textToSpeech():
# #     sys.path.insert(1, '../voice')
# #     from voiceToText import speech

# #     if request.method == 'POST':
# #         try:
# #             body = request.get_json()
# #             print(body)
# #             text = body['url']
# #             print(text)
# #             speech()
# #         except:
# #             return jsonify(result='ERROR : 400, bad request')