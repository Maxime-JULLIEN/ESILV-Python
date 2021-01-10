from flask import Flask, jsonify, request
import pandas as pd
import os
import numpy as np
import joblib
import re
from collections import Counter

app = Flask(__name__)

# Import Random Forest model to predict
model = joblib.load("./randForest.pkl")


def process_email(email):
    variables = ['make', 'address', 'all', '3d', 'our', 'over', 'remove', 'internet', 'order',
                 'mail', 'receive', 'will', 'people', 'report', 'addresses', 'free', 'business',
                 'email', 'you', 'credit', 'your', 'font', '000', 'money', 'hp', 'hpl', 'george',
                 '650', 'lab', 'labs', 'telnet', '857', 'data', '415', '85', 'technology', '1999',
                 'parts', 'pm', 'direct', 'cs', 'meeting', 'original', 'project', 're', 'edu', 'table',
                 'conference', ';', '(', '[', '!', '$', '#']

    # Find all word and some characters
    match_data = re.findall(r'\w+|\#|\?|\;|\(|\[|\!|\$', email)
    # lowercase all word to prevent the first uppercase
    match_data = [x.lower() for x in match_data]
    variables_cnt = Counter(match_data)  # Count the different word occurences

    def calcul_freq(x):
        return (float(0), 100 * variables_cnt[x] / len(match_data))[x in variables_cnt.keys()]

    results = list(map(calcul_freq, variables))  # Calcul the frequencies
    all_uppercase_sequence = re.findall(
        r"[A-Z]+", email)  # Find all uppercase sequences
    capital_run_length_total = sum(map(len, all_uppercase_sequence))

    if (capital_run_length_total == 0):
        results += [0, 0, 0]
        return results
    else:
        # capital_run_length_average
        results.append(capital_run_length_total / len(all_uppercase_sequence))
        # capital_run_length_longest
        results.append(len(max(all_uppercase_sequence, key=len)))
        # capital_run_length_total
        results.append(capital_run_length_total)

        return results


@ app.route("/api")
def hello():
    return "Hello World!"


@ app.route('/api/predict', methods=['POST'])
def predict():
    try:
        json_ = request.json  # Parse the request body
        # Check if the key content is in the body and is a string
        if 'content' not in json_ or not isinstance(json_["content"], str):
            return jsonify("Please enter a valid email.")
        # Process to get some word frequencies
        results = process_email(json_["content"])
        prediction = model.predict([results])  # Predict using the saved model
        prediction = (False, True)[prediction[0]]
        return jsonify({
            'prediction': prediction,
            'results': results
        })
    except Exception as e:
        # If an error occured, return this information to the client
        print("error")
        print(str(e))
        return jsonify("An error occured.")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
