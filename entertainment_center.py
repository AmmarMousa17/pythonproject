import fresh_tomatoes
import media
#Add instances from class Movies
#ADD 6 objects means 6 movies
IrretionalMan=media.Movie("Irretional Man", r"A professor in philosophy"\
, "https://cdn.flickeringmyth.com/wp-content/uploads/2015/08/irrational-man.jpg",\
"https://www.youtube.com/watch?v=hP8mPkyBntw")
matchpoint=media.Movie("Match Point", r"Lucky Tinnes Player",\
"http://www.woodyallenmovies.com/gifs/p/match-point-es.jpg",\
"https://www.youtube.com/watch?v=wISRAOb6xm0")
Clash=media.Movie("Clash",\
r"Revolution", "http://media.linkonlineworld.com/img/large/2016/6/18/2016_6_18_18_14_8_581.jpg", \
"https://www.youtube.com/watch?v=5km7bDqMNjo")
BeautifulMind=media.Movie("BeautifulMind ",\
"story of prof.Nash",\
"http://static.rogerebert.com/uploads/movie/movie_poster/a-beautiful-mind-2001/large_v1WdKm9qQPBfhoHanBP5XxzIBDU.jpg",\
"https://www.youtube.com/watch?v=aS_d0Ayjw4o")
Theory=media.Movie("Theory of everything ",\
"story of prof.Stephen Hawking",\
"https://upload.wikimedia.org/wikipedia/en/b/b8/Theory_of_Everything.jpg",\
"https://www.youtube.com/watch?v=Salz7uGp72c")
forrest=media.Movie("Forresr Gump","Nice Story","http://img.auctiva.com/imgdata/1/1/7/9/1/0/1/webimg/560104744_o.jpg","https://www.youtube.com/watch?v=uPIEn0M8su0")
#make a list  of films
movies=[BeautifulMind, IrretionalMan, matchpoint, Clash, Theory, forrest]
#open movie function in fresh tomatoes takes one argument as a list
fresh_tomatoes.open_movies_page(movies)
