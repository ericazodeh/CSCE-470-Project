from flask import Flask, render_template,url_for, request, redirect, jsonify
import requests
import json
import csv
import pandas as pd
print("Running")
app = Flask(__name__)
titleBasics = pd.read_csv("title.basics.tsv", sep="\t",header=0,dtype=str)
titleRatings = pd.read_csv("title.ratings.tsv", sep="\t",header=0,dtype=str)
titleCrew = pd.read_csv("title.crew.tsv", sep="\t",header=0,dtype=str)
titleName = pd.read_csv("name.basics.tsv", sep="\t",header=0,dtype=str)
@app.route("/<name>")
def index(name):
    #print(name)
    
    

    
    print(titleBasics.head())
    print(titleRatings.head())

    
    row = titleBasics.loc[titleBasics['originalTitle'] == name]

    rowId = row["tconst"].values.astype('str')[0]

    row2 = titleRatings.loc[titleRatings['tconst'] == rowId]
    row3 = titleCrew.loc[titleCrew['tconst'] == rowId]
    print (row2)
    averageRating =row2.iloc[0,1]
    numVotes =row2.iloc[0,2]
    print (averageRating)
    print (numVotes)
    print (row3)
    nameId =row3.iloc[0,1]
    row4 = titleName.loc[titleName['nconst'] == nameId]
    directorsName = row4.iloc[0,1]
    print(directorsName)
    
    stringTest = "Title: " + name +"<br>" + "Rating: " + averageRating + "<br>" + "Number of Votes: " + numVotes + "<br>" + "Directors Name: " + directorsName+ "<br>"
    return stringTest
    
 


    

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
