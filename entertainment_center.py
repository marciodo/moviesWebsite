# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import media
import fresh_tomatoes

####   TOY STORY
toy_story_params = []
# Title
toy_story_params.append("Toy Story")
# Storyline
toy_story_params.append("A story of a boy and his toys that come to life")
# Poster image link
toy_story_params.append("http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg")
# Trailer youtube link
toy_story_params.append("https://www.youtube.com/watch?v=vwyZH85NQC4")
# Director
toy_story_params.append("John Lasseter")
# List of actors
toy_story_params.append(["Tom Hanks", "Tim Allen", "Laurie Metcalf", "Annie Potts",
                         "John Ratzenberger", "Don Rickles", "Wallace Shawn",
                         "Jim Varney"])
# First release date
toy_story_params.append("November 19, 1995")
# Duration in minutes
toy_story_params.append(81)
# Budget in million dollars
toy_story_params.append(30)

toy_story = media.Movie(toy_story_params)


####   AVATAR
avatar_params = []
# Title
avatar_params.append("Avatar")
# Storyline
avatar_params.append("A marine on an alien planet")
# Poster image link
avatar_params.append("http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg")
# Trailer youtube link
avatar_params.append("https://www.youtube.com/watch?v=5PSNL1qE6VY")
# Director
avatar_params.append("James Cameron")
# List of actors
avatar_params.append(["Sam Worthington", "Zoe Saldana", "Sigourney Weaver", "Stephen Lang",
                      "Michelle Rodriguez", "Giovanni Ribisi", "Joel David Moore"])
# First release date
avatar_params.append("December 10, 2009")
# Duration in minutes
avatar_params.append(162)
# Budget in million dollars
avatar_params.append(237)

avatar = media.Movie(avatar_params)


####   DARK CITY
dark_city_params = []
# Title
dark_city_params.append("Dark City")
# Storyline
dark_city_params.append("A man struggles with memories of his past, including a wife he cannot remember, in a nightmarish world with no sun.")
# Poster image link
dark_city_params.append("https://compulsiveozblogger.files.wordpress.com/2013/10/dark_city_brd.jpg?w=650")
# Trailer youtube link
dark_city_params.append("https://www.youtube.com/watch?v=jSpowoKqSzc")
# Director
dark_city_params.append("Alex Proyas")
# List of actors
dark_city_params.append(["Rufus Sewell", "William Hurt", "Kiefer Sutherland", "Jennifer Connelly",
                         "Richard O'Brien", "Ian Richardson", "Bruce Spence", "Colin Friels",
                         "John Bluthal", "Mitchell Butel"])
# First release date
dark_city_params.append("February 27, 1998")
# Duration in minutes
dark_city_params.append(100)
# Budget in million dollars
dark_city_params.append(27)

dark_city = media.Movie(dark_city_params)


####   SCHOOL OF ROCK
school_of_rock_params = []
# Title
school_of_rock_params.append("School of Rock")
# Storyline
school_of_rock_params.append("After being kicked out of a rock band, Dewey Finn becomes a substitute teacher of a strict elementary private school, only to try and turn it into a rock band.")
# Poster image link
school_of_rock_params.append("http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg")
# Trailer youtube link
school_of_rock_params.append("https://www.youtube.com/watch?v=3PsUJFEBC74")
# Director
school_of_rock_params.append("Richard Linklater")
# List of actors
school_of_rock_params.append(["Jack Black", "Joan Cusack", "Mike White", "Sarah Silverman",
                              "Miranda Cosgrove", "Joey Gaydos Jr."])
# First release date
school_of_rock_params.append("October 3, 2003")
# Duration in minutes
school_of_rock_params.append(109)
# Budget in million dollars
school_of_rock_params.append(35)

school_of_rock = media.Movie(school_of_rock_params)


####   RATATOUILLE
ratatouille_params = []
# Title
ratatouille_params.append("Ratatouille")
# Storyline
ratatouille_params.append("A rat who can cook makes an unusual alliance with a young kitchen worker at a famous restaurant.")
# Poster image link
ratatouille_params.append("http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg")
# Trailer youtube link
ratatouille_params.append("https://www.youtube.com/watch?v=c3sBBRxDAqk")
# Director
ratatouille_params.append("Brad Bird")
# List of actors
ratatouille_params.append(["Patton Oswalt", "Ian Holm", "Lou Romano", "Brian Dennehy",
                           "Peter Sohn", "Peter O'Toole", "Brad Garrett", "Janeane Garofalo"])
# First release date
ratatouille_params.append("June 22, 2007")
# Duration in minutes
ratatouille_params.append(111)
# Budget in million dollars
ratatouille_params.append(150)

ratatouille = media.Movie(ratatouille_params)


####   MIDNIGHT IN PARIS
midnight_in_paris_params = []
# Title
midnight_in_paris_params.append("Midnight in Paris")
# Storyline
midnight_in_paris_params.append("While on a trip to Paris with his fiancee's family, a nostalgic screenwriter finds himself mysteriously going back to the 1920s every day at midnight.")
# Poster image link
midnight_in_paris_params.append("http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg")
# Trailer youtube link
midnight_in_paris_params.append("https://www.youtube.com/watch?v=atLg2wQQxvU")
# Director
midnight_in_paris_params.append("Woody Allen")
# List of actors
midnight_in_paris_params.append(["Owen Wilson", "Kathy Bates", "Adrien Brody", "Carla Bruni",
                                 "Marion Cotillard", "Rachel McAdams", "Michael Sheen"])
# First release date
midnight_in_paris_params.append("May 11, 2011")
# Duration in minutes
midnight_in_paris_params.append(94)
# Budget in million dollars
midnight_in_paris_params.append(17)

midnight_in_paris = media.Movie(midnight_in_paris_params)


####   HUNGER GAMES
hunger_games_params = []
# Title
hunger_games_params.append("The Hunger Games")
# Storyline
hunger_games_params.append("Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games, a televised competition in which two teenagers from each of the twelve Districts of Panem are chosen at random to fight to the death.")
# Poster image link
hunger_games_params.append("http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg")
# Trailer youtube link
hunger_games_params.append("https://www.youtube.com/watch?v=PbA63a7H0bo")
# Director
hunger_games_params.append("Gary Ross")
# List of actors
hunger_games_params.append(["Jennifer Lawrence", "Josh Hutcherson", "Liam Hemsworth", "Woody Harrelson",
                            "Elizabeth Banks", "Lenny Kravitz", "Stanley Tucci", "Donald Sutherland"])
# First release date
hunger_games_params.append("March 12, 2012")
# Duration in minutes
hunger_games_params.append(142)
# Budget in million dollars
hunger_games_params.append(78)

hunger_games = media.Movie(hunger_games_params)


movies = [toy_story, avatar, dark_city, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
