from flask import Flask, render_template,url_for, request, redirect, jsonify,flash, Markup
import requests
import json
import csv
import KNN_Predict
import pickle
import os
import random
# import data_preprocess

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
    image_names = os.listdir('static\Moviepictures')
    return render_template("index.html",image_names=image_names)

@app.route('/', methods=['GET','POST'])
def movies():
    
    textBoxInput = request.form['text']
    # Enter the query instead of "many years jerr"
    movies=KNN_Predict.predict(textBoxInput,training_vectors,Words)
    #return render_template("index.html")
    if movies=={}:
        message = Markup("<h1>'This Movie was not found!'</h1>")
        flash(message)
        return render_template("index.html")
    else:
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
def movie_info():
    movie_title = request.args.get('type')
    movie_info=dataset.loc[dataset['primaryTitle']==movie_title,['primaryTitle','startYear','genres','averageRating','numVotes','primaryName']]
    Name= movie_info['primaryTitle'].values[0]
    Year = movie_info['startYear'].values[0]
    Genres= movie_info['genres'].values[0]
    Director= movie_info['primaryName'].values[0]
    Rating= movie_info['averageRating'].values[0]
    Votes= movie_info['numVotes'].values[0]
    return render_template("movie_info.html", Name = Name, Year=Year, Genres = Genres,Director=Director,Rating=Rating,Votes=Votes)

@app.route('/movie_genre')
def movie_genre():
            return render_template("movie_genre.html")
  
  
   
@app.route('/movie_genre', methods=['GET', 'POST'])
def movie_genre_info():
    #genreTest= "Horror"
    genreTest= request.form['text2']

    try:
        r1 = random.randint(0, 100) #TODO: output more than 1 random movie between 0-10
        movie_genre= genreTest
        movie_info=dataset.loc[dataset['genres']==movie_genre,['primaryTitle','startYear','genres','averageRating','numVotes','primaryName']]
        Name= movie_info['primaryTitle'].values[r1]
        Year = movie_info['startYear'].values[r1]
        Genres= movie_info['genres'].values[r1]
        Director= movie_info['primaryName'].values[r1]
        Rating= movie_info['averageRating'].values[r1]
        Votes= movie_info['numVotes'].values[r1]

        return render_template("movie_genre_info.html", Name = Name, Year=Year, Genres = Genres,Director=Director,Rating=Rating,Votes=Votes)
    except: #Does not work for exception
        message = Markup("<h1>'This Genre was not found!'</h1>")
        flash(message)
        return render_template("movie_genre.html")
   

  

if __name__ == "__main__":
    app.run(debug=True)
