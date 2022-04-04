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

with open('data/dataset_pkl', 'rb') as f:
    dataset= pickle.load(f)


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
    for movie, value in sorted(movies.items(), key = lambda x: x[1],reverse=True):
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

@app.route('/movies', methods=['GET', 'POST'])
def movies():
    movie_title = request.args.get('type')
    movie_info=dataset.loc[dataset['primaryTitle']==movie_title,['primaryTitle','startYear','genres','averageRating','numVotes','primaryName']]
    Name= movie_info['primaryTitle'].values[0]
    Year = movie_info['startYear'].values[0]
    Genres= movie_info['genres'].values[0]
    Director= movie_info['primaryName'].values[0]
    Rating= movie_info['averageRating'].values[0]
    Votes= movie_info['numVotes'].values[0]
    return render_template("movie_info.html", Name = Name, Year=Year, Genres = Genres,Director=Director,Rating=Rating,Votes=Votes)



  

if __name__ == "__main__":
    app.run(debug=True)
