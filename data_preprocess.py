import pandas as pd
import pickle


titleBasics = pd.read_csv("data/title.basics.tsv", sep="\t",header=0,dtype=str)
titleRatings = pd.read_csv("data/title.ratings.tsv", sep="\t",header=0,dtype=str)
titleCrew = pd.read_csv("data/title.crew.tsv", sep="\t",header=0,dtype=str)
titleName = pd.read_csv("data/name.basics.tsv", sep="\t",header=0,dtype=str)

# merge all the dataframes
title_data=pd.merge(titleBasics[['tconst','primaryTitle','originalTitle','startYear','genres','runtimeMinutes']], titleRatings, on='tconst')
directors_data=pd.merge(titleCrew, titleName, left_on='directors', right_on='nconst')
total_data=pd.merge(title_data, directors_data[['tconst','primaryName']], on='tconst')
name=[]
for i in range(len(total_data)):
    if total_data.iloc[i]['primaryTitle'] == total_data.iloc[i]['originalTitle']:
        name.append(str(total_data.iloc[i]['primaryTitle']))
    else:
        name.append(str(total_data.iloc[i]['primaryTitle']) +" "+ str(total_data.iloc[i]['originalTitle']))
total_data['name']=name
# m=total_data.loc[total_data['primaryTitle']=="Procesión de las hijas de María de la parroquia de Sans"]
# print(m)
with open('data/dataset_pkl', 'wb') as f:
     pickle.dump(total_data, f)





