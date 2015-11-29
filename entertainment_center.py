import fresh_tomatoes
import media

#Below are the instances for the movie objects. The cast for each movie is declared above movie instantiation so they can be included in the movie constructor
dark_knight_cast = ["Christian Bale", "Heath Ledger", "Aaron Eckhart", "Michael Caine", "Maggie Gyllenhaal", "Gary Oldman", "Morgan Freeman"]
dark_knight = media.Movie("The Dark Knight",
                          "Batman faces off against the Joker in a battle to save Gotham.",
                          "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                          "July 18, 2008", dark_knight_cast, "PG-13")


age_of_ultron_cast = ["Robert Downey Jr.", "Chris Hemsworth", "Mark Ruffalo", "Chris Evans", "Scarlett Johansson", "Jeremy Renner", "James Spader", "Samuel L. Jackson"]
age_of_ultron = media.Movie("Avengers: Age of Ultron",
                            "The Avengers face off against genocidal robot, Ultron",
                            "http://i2.wp.com/bitcast-a-sm.bitgravity.com/slashfilm/wp/wp-content/images/Avengers-Age-of-Ultron-Poster.jpg",
                            "https://www.youtube.com/watch?v=tmeOjFno6Do",
                            "May 1, 2015", age_of_ultron_cast, "PG-13")

beautiful_mind_cast=["Russell Crowe", "Ed Harris", "Jennifer Connelly", "Christopher Plummer", "Paul Bettany"]
beautiful_mind = media.Movie("A Beautiful Mind",
                             "Brilliant mathematician, John Nash, his own mind and discovers the gift of a beautiful heart",
                             "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg",
                             "https://www.youtube.com/watch?v=YWwAOutgWBQ",
                             "December 21, 2001", beautiful_mind_cast, "PG-13")

guardians_cast=["Chris Pratt", "Zoe Saldana", "Dave Bautista", "Vin Diesel", "Bradley Cooper", "Lee Pace"]
guardians = media.Movie("Guardians of the Galaxy",
                        "An unlikely band of heroes come together to save a planet from total anihilation",
                        "http://1.media.dorkly.cvcdn.com/26/95/18b149286ca6f2920e017bd5d2ffcbf5.jpg",
                        "https://www.youtube.com/watch?v=B16Bo47KS2g",
                        "August 1, 2014", guardians_cast, "PG-13")

tron_legacy_cast=["Jeff Bridges", "Garrett Hedlund", "Olivia Wilde", "Bruce Boxleitner"]
tron_legacy = media.Movie("TRON: LEGACY",
                          "The son of renowned programmer, Kevin Flynn, goes on an adventure in a mysterious place known as: The Grid",
                          "http://www.impawards.com/2010/posters/tron_legacy_ver11.jpg",
                          "https://www.youtube.com/watch?v=L9szn1QQfas",
                          "December 17, 2010", tron_legacy_cast, "PG")

scott_pilgrim_cast=["Michael Cera", "Mary Elizabeth Winstead", "Kieran Culkin", "Chris Evans", "Anna Kendrick"]
scott_pilgrim = media.Movie("Scott Pilgrim Vs. The World",
                            "Scott Pilgrim just wants to be with Ramona Flowers but first, he must defeat her seven evil exes.",
                            "http://images.moviepostershop.com/scott-pilgrim-vs-the-world-movie-poster-2010-1020561018.jpg",
                            "https://www.youtube.com/watch?v=7wd5KEaOtm4",
                            "August 13, 2010", scott_pilgrim_cast, "PG-13")

#Create movie list and pass it in to the web page constructor. 
movies = [dark_knight, age_of_ultron, beautiful_mind, guardians, tron_legacy, scott_pilgrim]
fresh_tomatoes.open_movies_page(movies)
                        
