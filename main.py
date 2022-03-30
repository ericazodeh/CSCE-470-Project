from flask import Flask, render_template,url_for, request, redirect, jsonify
import requests
import json
import csv
import KNN_Predict
import pickle

print("Running")
app = Flask(__name__)


@app.route("/")
def index():
    
    with open('data/training_pkl', 'rb') as f:
        training_vectors= pickle.load(f)
    
    with open('data/word_bank_pkl', 'rb') as f:
        Words= pickle.load(f)

    # Enter the query instead of "many years jerr"
    movies=KNN_Predict.predict("many years jerr",training_vectors,Words)
    
    return movies
  

if __name__ == "__main__":
    app.run(debug=True)
