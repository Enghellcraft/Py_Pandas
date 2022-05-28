import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

userHeader = ['user_id', 'gender', 'age', 'ocupation', 'zip']
users = pd.read_table('dataset/users.txt', engine='python', sep='::', header=None, names=userHeader)
users.head()

ratingHeader = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('dataset/ratings.txt', engine='python', sep='::', header=None, names=ratingHeader)
ratings.head()

movieHeader = ['movie_id', 'title', 'genders']
movies = pd.read_table('dataset/movies.txt', engine='python', sep='::', header=None, 
 names=movieHeader, encoding='latin-1')
movies.head()

mergeRatings = pd.merge(users, ratings, on='user_id')
mergeRatings.head()

mergeRatings = mergeRatings.drop(['user_id','zip','timestamp','ocupation'], axis=1)
mergeRatings.head()

merge = pd.merge(mergeRatings, movies)
merge.head()

colors = ['magenta','tan','mediumseagreen','orange','blueviolet', 'gold', 'salmon', 'limegreen']
merge.groupby('gender').size().plot(kind='bar', color=colors)
avgRatings = merge.groupby(['movie_id', 'title']).mean()
print ('Media del rating:', avgRatings['rating'][:10])
dataRatings = merge.groupby(['movie_id', 'title'])['rating'].agg(['mean', 'sum', 'count', 'std'])
print ('Info estadística del rating:', dataRatings[:10])
plt.show()

