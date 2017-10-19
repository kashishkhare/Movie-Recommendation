import dill
from nltk.book import *
file = open("movie_model.p","rb")
movie_name=dill.load(file)
movie_genre=dill.load(file)
movie_ratings=dill.load(file)
file.close
def recommend(my_movie,genre,rating):
    my_movie = my_movie
    my_genre = genre
    my_rating = rating
    print ("Recommended movies for you")
    print ("Movie".rjust(15),"Genre".rjust(25),"Rating".rjust(10))
    rating_list =[r for r in movie_ratings.keys() if (movie_ratings[r]<=(my_rating+1) and movie_ratings[r]>=(my_rating-1))]
    genre_list = [r for r in movie_genre.keys() for g in my_genre if g in movie_genre[r]]
    #print (rating_list)
    #print (genre_list)
    ## -----Frequency distribution of genre list--------
    genre_fdist = FreqDist(genre_list)
    common_fdist={}
    ##-------Common items in rating list and genre frequency distribution dictionary
    for ids in genre_fdist:
        if ids in rating_list:
            common_fdist[ids]=genre_fdist[ids]
    #print (fdist1.items())
    ##----------------Special case of Children's movies---------------------
    childs_fdist={}
    if "Children's" in my_genre:
        for ids in common_fdist:
            if "Children's" in movie_genre[ids]:
                childs_fdist[ids]=common_fdist[ids]
        common_fdist=childs_fdist
    #print (childs_fdist.items())
    i=0
    #--------sorting common list based on highest number of genre match in any movie
    for w in sorted(common_fdist, key=common_fdist.get, reverse=True):
        if i<10:
            print (repr(movie_name[w]).rjust(15), repr(movie_genre[w]).rjust(25), repr(movie_ratings[w]).rjust(10))
            i+=1
