import dill
# movies are in format MovieID::Title::Genres
# title consist of name and year released
# genre are pipe-seperated
file = open ("ml-1m/movies.dat","r")
movie_name={} #movie id and name
movie_genre={} #movie id and genre
for line in file:
    line=line[:-1]
    moviename = line[line.find("::")+2:line.find("(")-1]
    movieid=line[:line.find("::")]
    movie_name[movieid]=moviename
    genre = line[line.find(")::")+3:]
    movie_genre[movieid]=genre.split("|")
file.close()
file =open("ml-1m/ratings.dat","r")
# ratings are in format UserID::MovieID::Rating::Timestamp
ratings={} 
movie_ratings={}  #movie id and rating
for file_line in file:
    line=file_line.split("::")
    r = int(line[2]) #rating by individual
    # taking average rating of a movie as given by different users
    if line[1] not in ratings:
        ratings[line[1]]=(r,1)
    else:
         rate=ratings[line[1]][0]+r
         count= ratings[line[1]][1]+1
         ratings[line[1]]=(rate,count)
for item in ratings:
    movie_ratings[item]=round(ratings[item][0]/ratings[item][1],1)
file.close()
##ids = [(mov_id,name) for (mov_id,name) in movie_name.items()]
##print (ids[:5])
# user information Pg 26 oreilly
file= open("ml-1m/ratings.dat","r")
user={}
for file_line in file:
    line=file_line.split("::")
    #print (line)
    user.setdefault(line[0],{})
    user[line[0]][movie_name[line[1]]] = float(line[2])
file.close()
user.setdefault("6041",{})
userid="6041"
movieid_rating=[("1954",3.9),("3876",2),("3948",3),("318",4.5),("2571",5),("367",3.5),("1240",5),("362",3.5)]
for (movieid,rating) in movieid_rating:
    user[userid][movie_name[movieid]]=float(rating)

#flipping movies and users
movies={}
for u in user:
    for movie in user[u]:
        movies.setdefault(movie,{})
        # flip movie and user
        movies[movie][u] = user[u][movie]
    

file = open ("movie_model.p","wb")
dill.dump(movie_name,file)
dill.dump(movie_genre,file)
dill.dump (movie_ratings,file)
dill.dump (user,file)
dill.dump (movies,file)
file.close
file = open ("movie_model.p","rb")
dict1=dill.load(file)
dict2=dill.load(file)
dict3=dill.load(file)
dict4=dill.load(file)
dict5 = dill.load(file)
for i in range(4):
##  print(dict1.popitem())
##  print (dict2.popitem())
##  print (dict3.popitem())
##  print (dict4.popitem())
  print (dict5.popitem())
file.close
