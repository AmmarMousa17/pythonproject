import fresh_tomatoes
import media
"""Add instances from class Movies"""
"""ADD 6 objects means 6 movies"""
irretional_man = media.Movie(
    "Irretional Man",
    r"A professor in philosophy",
    r"https://cdn.flickeringmyth.com/wp-content/uploads/2015/08/irrational-man.jpg",  #NOQA
    r"https://www.youtube.com/watch?v=hP8mPkyBntw")
match_point = media.Movie("Match Point",
                        r"Lucky Tinnes Player",
                        r"http://www.woodyallenmovies.com/gifs/p/match-point-es.jpg", #NOQA
                        r"https://www.youtube.com/watch?v=wISRAOb6xm0")
clash = media.Movie("Clash",
                  r"Revolution",
                  r"http://media.linkonlineworld.com/img/large/2016/6/18/2016_6_18_18_14_8_581.jpg",  #NOQA
                  r"https://www.youtube.com/watch?v=5km7bDqMNjo")
beautiful_mind = media.Movie("BeautifulMind ",
                           "story of prof.Nash",
                           "http://static.rogerebert.com/uploads/movie/movie_poster/a-beautiful-mind-2001/large_v1WdKm9qQPBfhoHanBP5XxzIBDU.jpg",  #NOQA
                           "https://www.youtube.com/watch?v=aS_d0Ayjw4o")
theory = media.Movie("Theory of everything ",
                   r"story of prof.Stephen Hawking",
                   r"https://upload.wikimedia.org/wikipedia/en/b/b8/Theory_of_Everything.jpg",  #NOQA
                   r"https://www.youtube.com/watch?v=Salz7uGp72c")
forrest = media.Movie("Forresr Gump",
                   r"Nice Story",
                   r"http://img.auctiva.com/imgdata/1/1/7/9/1/0/1/webimg/560104744_o.jpg",  #NOQA
                   r"https://www.youtube.com/watch?v=uPIEn0M8su0")

movies = [beautiful_mind, irretional_man, match_point, clash, theory, forrest]
"""make a list  of films"""

fresh_tomatoes.open_movies_page(movies)
"""open movie function in fresh tomatoes takes one argument as a list"""
