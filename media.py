# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/m-1013629057

import webbrowser


class Movie():
    """This class provides a way to store movie related information"""

    def __init__(self, movie_params):
        """ Initialize instance of class Movie
            movie_params[0] -> title
            movie_params[1] -> storyline
            movie_params[2] -> poster image link
            movie_params[3] -> trailer youtube link
            movie_params[4] -> director
            movie_params[5] -> list of actors
            movie_params[6] -> first release date
            movie_params[7] -> duration in minutes
            movie_params[8] -> budget in million dollars
        """
        self.title = movie_params[0]
        self.storyline = movie_params[1]
        self.poster_image_url = movie_params[2]
        self.trailer_youtube_url = movie_params[3]
        self.director = movie_params[4]
        self.actors = movie_params[5]
        self.release_date = movie_params[6]
        self.duration = movie_params[7]
        self.budget = movie_params[8]

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
