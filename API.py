from flask import Flask, jsonify, request
import pandas as pd
import os

# from sklearn.externals import joblib
# from sklearn.linear_model import LinearRegression

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


# @app.route("/predict", methods=['POST'])
# def predict():
#     if request.method == 'POST':
#         try:
#             data = request.get_json()
#             years_of_experience = float(data["yearsOfExperience"])

#             lin_reg = joblib.load("./linear_regression_model.pkl")
#         except ValueError:
#             return jsonify("Please enter a number.")

#         return jsonify(lin_reg.predict(years_of_experience).tolist())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8005)
