# -*- coding: utf-8 -*-
"""server.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TY9RReRGzHbFzJgZrbU-ggtqqEYoIvQP

### In this file, we will use the flask web framework to handle the POST requests that we will get from the request.py.
"""
#import requests
import json
import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb')) # created the instance of the Flask() and loaded the model into the model.

@app.route('/api',methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([[np.array(data['exp'])]])
    output = prediction[0]
    return jsonify(output)

if __name__ == '__main__':
    app.run(port=5000, debug=True)