import webbrowser
class Movie:
    def __init__(self,trailer_youtube_url,cartaz,title,resumo):
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = cartaz
        self.title = title
        self.resumo = resumo
    def mostra_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
