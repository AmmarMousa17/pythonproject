import webbrowser
class Movie():
    #Make Constructor
    def __init__(self,title,story,poster_image,trailer):
        self.title=title
        self.storyline=story
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer
    #method to open trailer on browser
    def trailer(self):
        webbrowser.open(self.trailer_youtube_url)


