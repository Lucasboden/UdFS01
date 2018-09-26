import webbrowser


class Movie:
    def __init__(self, trailer_youtube_url, cartaz, title, resumo):
        """Cria instancia da classe Movie com parametros passados"""
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = cartaz
        self.title = title
        self.resumo = resumo

    def mostra_trailer(self):
        """Funcao que mostra na tela o trailer do filme."""
        webbrowser.open(self.trailer_youtube_url)
