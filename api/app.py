from flask import Flask, jsonify, request
import pandas as pd
import os
import numpy as np
import joblib
import re
from collections import Counter

app = Flask(__name__)

model = joblib.load("./randForest.pkl")


def process_email(email):
    variables = ['make', 'address', 'all', '3d', 'our', 'over', 'remove', 'internet', 'order',
                 'mail', 'receive', 'will', 'people', 'report', 'addresses', 'free', 'business',
                 'email', 'you', 'credit', 'your', 'font', '000', 'money', 'hp', 'hpl', 'george',
                 '650', 'lab', 'labs', 'telnet', '857', 'data', '415', '85', 'technology', '1999',
                 'parts', 'pm', 'direct', 'cs', 'meeting', 'original', 'project', 're', 'edu', 'table',
                 'conference', ';', '(', '[', '!', '$', '#']

    text_split = re.findall(r'\w+|\#|\?|\;|\(|\[|\!|\$', email)
    text_split = [x.lower() for x in text_split]
    text_split_count = Counter(text_split)

    def calcul_freq(x):
        return (float(0), 100 * text_split_count[x] / len(text_split))[x in text_split_count.keys()]

    results = list(map(calcul_freq, variables))
    all_uppercase_sequence = re.findall(r"[A-Z]+", email)
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
        json_ = request.json
        if 'content' not in json_ or not isinstance(json_["content"], str):
            return jsonify("Please enter a valid email.")
        results = process_email(json_["content"])
        prediction = model.predict([results])
        prediction = (False, True)[prediction[0]]
        return jsonify({
            'prediction': prediction,
            'results': results
        })
    except Exception as e:
        print("error")
        print(str(e))
        return jsonify("An error occured.")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
