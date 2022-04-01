from flask import Flask, render_template,url_for, request, redirect, jsonify
import requests
import json
import csv
import KNN_Predict
import pickle


print("Running")
app = Flask(__name__)

with open('data/training_pkl', 'rb') as f:
        training_vectors= pickle.load(f)
    
with open('data/word_bank_pkl', 'rb') as f:
    Words= pickle.load(f)


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def pickMovies():
    
    textBoxInput = request.form['text']
    # Enter the query instead of "many years jerr"
    movies=KNN_Predict.predict(textBoxInput,training_vectors,Words)
    #return render_template("index.html")
    i = 1
    moviePicks ={
        "first" : {"" : 0.0},
        "second" : {"" : 0.0},
        "third" : {"" : 0.0},
        "fourth" : {"" : 0.0},
        "fifth" : {"" : 0.0}
    }
    firstMovie = secondMovie = thirdMovie = fourthMovie = fifthMovie = "No movie prediction"
    for movie, value in sorted(movies.items(), key = lambda x: x[1]):
        if i == 1:
            #moviePicks["first"] = {movie : value}
            firstMovie = movie
        elif i == 2:
            #moviePicks["second"] = {movie : value}
            secondMovie = movie
        elif i == 3:
            #moviePicks["third"] = {movie : value}
            thirdMovie = movie
        elif i == 4:
            #moviePicks["fourth"] = {movie : value}
            fourthMovie = movie
        elif i == 5:
            #moviePicks["fifth"] = {movie : value}
            fifthMovie = movie
        
        i += 1

    hi = "hi"
    return render_template("movies.html",movies = movies, firstMovie=firstMovie, secondMovie = secondMovie,thirdMovie = thirdMovie,fourthMovie = fourthMovie, fifthMovie = fifthMovie)

@app.route('/movies', methods=['POST'])
def getMovieInfo():
    return "This part is not done yet"



  

if __name__ == "__main__":
    app.run(debug=True)
