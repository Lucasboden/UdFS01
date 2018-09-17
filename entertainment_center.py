import media
import fresh_tomatoes

# Filme do bambi. Quem nao chorou com a morte da mae dele?
bambi = media.Movie("https://www.youtube.com/watch?v=nLvX-erABqY",
                    ("https://lumiere-a.akamaihd.net/v1/images/p_bambi_digital"
                        "hd_1f041240.png?region=0,0,400,400"),
                    "Bambi",
                    "Historia de um veado que perde a mae ainda novo.")

# Filme dos 101 dalmatas.
# Adaptacao pra vida real, mas o desenho e mais legal.
dalmatas = media.Movie("https://www.youtube.com/watch?v=EMbYwrt6vgM",
                       ("https://www.google.com.br/url?sa=i&rct=j&q=&esrc="
                        "s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiOg"
                        "-PShcLdAhXMjJAKHRvhB1sQjRx6BAgBEAU&url=https%3A%2"
                        "F%2Fwww.youtube.com%2Fwatch%3Fv%3DvPvbpYIbkL0&psi"
                        "g=AOvVaw3cGe8yYQ5sofYEDvUxZxgV&ust=15372738867"
                        "21968"),
                       "101 Dalmatas",
                       ("101 cachorros que sao sequestrados por uma mulher"
                        "cruel que quer transforma-los em roupa."))


# Filme Moulin Rouge. Excelente filme pra ver com a namorada
moulin_rouge = media.Movie("https://www.youtube.com/watch?v=SyZDaTZSFuo",
                           ("https://images-na.ssl-images-amazon.com/images"
                            "/I/51E4KFHE9EL.jpg"), "Moulin Rouge",
                           ("Rapaz pobre se apaixona por "
                            "dancarina de uma das casas de "
                            "espetaculo mais famosas do mundo e os dois"
                            "vivem uma historia de amor muito dificil."))


# Lista dos filmes que serao exibidos no site.
# Para colocar mais no site,
# basta criar novas instancias e adiciona-las na lista
movies = [bambi, dalmatas, moulin_rouge]

# Chama a funcao pra criar a pagina HTML
fresh_tomatoes.open_movies_page(movies)
