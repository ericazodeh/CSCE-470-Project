from flask import Flask, render_template,url_for, request, redirect, jsonify,flash, Markup
import requests
import json
import csv
import KNN_Predict
import pickle
import os
import random
# import data_preprocess
currentGenre=" "
page=0

print("Running")
app = Flask(__name__)

with open('data/training_pkl', 'rb') as t:
        training_vectors= pickle.load(t)

with open('data/word_bank_pkl', 'rb') as w:
    Words= pickle.load(w)

with open('data/dataset_pkl', 'rb') as d:
    dataset= pickle.load(d)

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
    if len(movies)==0:
        message = Markup("<h1>This Movie was not found!</h1>")
        flash(message)
        image_names = os.listdir('static\Moviepictures')
        return render_template("index.html",image_names=image_names)
    else:
        i = 1
        moviePicks ={
            "first" : {"" : 0.0},
            "second" : {"" : 0.0},
            "third" : {"" : 0.0},
            "fourth" : {"" : 0.0},
            "fifth" : {"" : 0.0}
        }
        firstMovie = secondMovie = thirdMovie = fourthMovie = fifthMovie = "None"
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

        return render_template("movies.html",movies = movies, firstMovie=firstMovie, secondMovie = secondMovie,thirdMovie = thirdMovie,fourthMovie = fourthMovie, fifthMovie = fifthMovie,value=value)

@app.route('/movie_info', methods=['GET', 'POST'])
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
    global currentGenre
    global page
    try:
        genreTest= request.form['text2']
        currentGenre = genreTest.capitalize()
        #PageNumberTest = request.form['text2'] 
        page = 0
    except:
        PageNumberTest = int(request.form['text3'])
        page = PageNumberTest-1
        print("this worked ")


    
    try:
        #r1 = random.randint(0, 100) #TODO: output more than 1 random movie between 0-10
        entry0=0 + 5*page
        entry1=1 + 5*page
        entry2=2 + 5*page
        entry3=3 + 5*page
        entry4=4 + 5*page
        movie_genre= currentGenre
        movie_info= dataset.loc[dataset['genres']==movie_genre,['primaryTitle','startYear','genres','averageRating','numVotes','primaryName']]
        Name0= movie_info['primaryTitle'].values[entry0]
        Year0 = movie_info['startYear'].values[entry0]
        Genres0= movie_info['genres'].values[entry0]
        Director0= movie_info['primaryName'].values[entry0]
        Rating0= movie_info['averageRating'].values[entry0]
        Votes0= movie_info['numVotes'].values[entry0]

        Name1= movie_info['primaryTitle'].values[entry1]
        Year1 = movie_info['startYear'].values[entry1]
        Genres1= movie_info['genres'].values[entry1]
        Director1= movie_info['primaryName'].values[entry1]
        Rating1= movie_info['averageRating'].values[entry1]
        Votes1= movie_info['numVotes'].values[entry1]


        Name2= movie_info['primaryTitle'].values[entry2]
        Year2 = movie_info['startYear'].values[entry2]
        Genres2= movie_info['genres'].values[entry2]
        Director2= movie_info['primaryName'].values[entry2]
        Rating2= movie_info['averageRating'].values[entry2]
        Votes2= movie_info['numVotes'].values[entry2]


        Name3= movie_info['primaryTitle'].values[entry3]
        Year3 = movie_info['startYear'].values[entry3]
        Genres3= movie_info['genres'].values[entry3]
        Director3= movie_info['primaryName'].values[entry3]
        Rating3= movie_info['averageRating'].values[entry3]
        Votes3= movie_info['numVotes'].values[entry3]


        Name4= movie_info['primaryTitle'].values[entry4]
        Year4 = movie_info['startYear'].values[entry4]
        Genres4= movie_info['genres'].values[entry4]
        Director4= movie_info['primaryName'].values[entry4]
        Rating4= movie_info['averageRating'].values[entry4]
        Votes4= movie_info['numVotes'].values[entry4]


        return render_template("movie_genre_info.html",PageNum=page+1, Name0 = Name0, Year0=Year0, Genres0 = Genres0,Director0=Director0,Rating0=Rating0,Votes0=Votes0,
        Name1 = Name1, Year1=Year1, Genres1 = Genres1,Director1=Director1,Rating1=Rating1,Votes1=Votes1,
        Name2 = Name2, Year2=Year2, Genres2 = Genres2,Director2=Director2,Rating2=Rating2,Votes2=Votes2,
        Name3 = Name3, Year3=Year3, Genres3 = Genres3,Director3=Director3,Rating3=Rating3,Votes3=Votes3,
        Name4 = Name4, Year4=Year4, Genres4 = Genres4,Director4=Director4,Rating4=Rating4,Votes4=Votes4)
    except:
       message = Markup("<h1>'This Genre was not found!'</h1>")
       flash(message)
       return render_template("movie_genre.html")





   

  

if __name__ == "__main__":
    app.config['SECRET_KEY']="123"
    app.run(debug=True)
