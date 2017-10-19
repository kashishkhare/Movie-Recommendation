import dill
#from nltk.book import *
from math import sqrt
file = open("movie_model.p","rb")
movie_name=dill.load(file)
movie_genre=dill.load(file)
movie_ratings=dill.load(file)
users = dill.load(file)
movies=dill.load(file)
file.close
def similarity(movie_list,m1,m2):
    shared={}
    for user in movie_list[m1]:
        if user in movie_list[m2]:
            shared[user]=1
    if len(shared)==0 :
        return 0
    sum_of_sqr = sum([pow(movie_list[m1][user]-movie_list[m2][user],2)
                      for user in movie_list[m1] if user in movie_list[m2]])
    return 1/(1+sqrt(sum_of_sqr))

def topMatches(movie):
    scores=[(similarity(movies,movie,m2),m2) for m2 in movies if m2!=movie]
    scores.sort()
    scores.reverse()
    recommend_list = scores[0:10]
    print ("Recommended movies-------------------------------------------------------")
    print ("Movie".rjust(10),"Similarity".rjust(10),"Rating".rjust(10),"Genre")
    for ids in movie_name.keys():
        if movie==movie_name[ids]:
            movie_id = ids
    for (sim,movie) in recommend_list:
        for ids in movie_name.keys():
            if movie==movie_name[ids]:
                movie_id = ids
        print (movie.rjust(10),repr(sim).rjust(10),repr(movie_ratings[movie_id]).rjust(10),movie_genre[movie_id])

def getRecommendations(person):
    totals={}
    simSums={}
    for other in users:
        if other == person:
            continue
        sim = similarity(users,person,other)
        if sim<=0:
            continue
        for item in users[other]:
            if item not in users[person] or users[person][item]==0:
                totals.setdefault(item,0)
                totals[item]+=users[other][item]*sim
                simSums.setdefault(item,0)
                simSums[item]+=sim
    rankings=[(total/simSums[item],item) for item,total in totals.items()]
    rankings.sort()
    rankings.reverse()
    print (len(rankings))
    return rankings[:30]
    
        
