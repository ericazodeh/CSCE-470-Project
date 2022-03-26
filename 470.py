from flask import Flask, render_template,url_for, request, redirect, jsonify
import requests
import json
import csv
print("Running")
app = Flask(__name__)

@app.route("/")
def index():
    tsv_file = open("data.tsv")
    read_tsv = csv.reader(tsv_file, delimiter="\t")
    i = 0
    rows = []
    for row in read_tsv:
        rows.append(row)

    return rows[5][0]

    

if __name__ == "__main__":
    app.run(debug=True)