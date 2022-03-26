from flask import Flask, render_template,url_for, request, redirect, jsonify
import requests
import json
import csv
import pandas as pd
print("Running")
app = Flask(__name__)
#change these w/ your file name
nameBasics = open("name.basics.tsv")
titleBasics = open("title.basics.tsv")
titleRatings = open("title.ratings.tsv")
titleCrew = open("title.crew.tsv")


def printData(name):
    #open file
    title = open(name)
    read_tsv = csv.reader(title, delimiter="\t")
    i = 0
    #print file name 1st
    print(name)
    for row in read_tsv:
        #only show the 1st 5 lines
        if i == 5:
            break
        i+=1
        print(row)
    print()



#do this for all files
listOfData = ["name.basics.tsv","title.basics.tsv","title.ratings.tsv","title.crew.tsv"]
for title in listOfData:
    printData(title)


def printDataFrame(name):
    print(name)
    title = open(name,'r', encoding='utf-8')
    read_tsv = pd.read_csv(title, sep="\t",header=0,dtype=str)
    print(read_tsv.head())

for title in listOfData:
    printDataFrame(title)

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