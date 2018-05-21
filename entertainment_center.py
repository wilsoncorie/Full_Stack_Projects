import media
import fresh_tomatoes


# first instances of the movie file
# contain title, information, poster, video
black_panther=media.Movie("Black Panther","Black Panther is a fictional"
                          "superhero appearing in American comic books"
                          "published by Marvel Comics. "
                          ,"https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg" # NOQA
                          ,"https://www.youtube.com/watch?v=xjDjIWPwcPU") # NOQA

# second instances of the movie file
# contain title, information, poster, video
atl=media.Movie("ATL","As four friends prepare for life after high school,"
                "different challenges bring about turning points in each of"
                "their lives. The dramas unfold and resolve at their local "
                "rollerskating rink, Cascade.",
                "https://upload.wikimedia.org/wikipedia/en/4/42/ATL_theatrical_poster.jpg", # NOQA
                "https://www.youtube.com/watch?v=jHi9GK7fvkE") # NOQA

# third instances of the movie file
# contain title, information, poster, video
drum=media.Movie("Drumline","A band director recruits a Harlem street drummer"
                 "to play at a Southern university. ",
                 "https://upload.wikimedia.org/wikipedia/en/5/55/Drumlineposter2002.jpg", # NOQA
                 "https://www.youtube.com/watch?v=3J_LqCnPvgI") # NOQA

# fourth instances of the movie file
# contain title, information, poster, video
waiting=media.Movie("Waiting to exhale","Based on Terry McMillan's novel, "
                    "this film follows four very different African-American"
                    " women and their relationships with the male gender. ",
                    "https://upload.wikimedia.org/wikipedia/en/c/ca/WaitingExhale.jpg", # NOQA
                    "https://www.youtube.com/results?search_query=waiting+to+exhale+trailer") # NOQA

# fifth instances of the movie file
# contain title, information, poster, video
love_jones=media.Movie("Love Jones","Say hello to Darious Lovehall (Larenz Tate)"
                       "and Nina Mosley (Nia Long), two confused lovebirds"
                       "who discover that you can never underestimate the power"
                       "of a love jones.",
                       "https://upload.wikimedia.org/wikipedia/en/2/2c/LoveJonesMovie.jpg", # NOQA
                       "https://www.youtube.com/watch?v=xNMoQ_Cqt4E") # NOQA

# sixth instances of the movie file
# contain title, information, poster, video
the_wood=media.Movie("The Wood","While dealing with a friend's cold feet on "
                     "his wedding day, a writer reminisces about his youth "
                     "with his best friends. "
                      ,"https://upload.wikimedia.org/wikipedia/en/f/f7/Wood_poster.jpg" # NOQA
                      ,"https://www.youtube.com/watch?v=koP2IdQhA_I") # NOQA

# seventh instances of the movie file
# contain title, information, poster, video
uncle_drew=media.Movie("Uncle Drew","After draining his life savings to"
                       " enter a team in the Rucker Classic street ball"
                       "tournament in Harlem, Dax (Lil Rel Howery) is dealt"
                       "a series of unfortunate setbacks",
                       "https://upload.wikimedia.org/wikipedia/en/3/30/Uncle_Drew_poster.png" # NOQA
                       ,"https://www.youtube.com/watch?v=21CbEte27-I") # NOQA



# an array of movies stored in a movie variable
movies = [black_panther,atl,drum,waiting,
          love_jones,the_wood,uncle_drew]

# file fresh tomatoes to open the function open movie file
fresh_tomatoes.open_movies_page(movies)
