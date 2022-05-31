import pandas as pd
import numpy as np
import pickle

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def main():
    return 'Container is up & running'


@app.route('/SimpleLinearRegression/Predict')
def predict():
    height = request.args.get('height')
    _input = np.array([height], dtype=float).reshape(-1, 1)

    with open("linear_regression.pkl", "rb") as pickle_in:
        linear_regression = pickle.load(pickle_in)
        result = linear_regression.predict(_input)
        return "The predict weight against height {0} is {1}".format(height, round(result[0], 2))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
