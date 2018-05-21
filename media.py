import webbrowser

class Movie(): # class Movie define to store methods and instances

    # constructor with init defined
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title  # instance variable defined for title
        self.storyline = movie_storyline # instance variable defined for storyline
        self.poster_image_url = poster_image # instance variable defined for image
        self.trailer_youtube_url = trailer_youtube # instance variable defined for video
        
    # instance method created to open instance youtube video   
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url) #module called to open video
        
