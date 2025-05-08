import requests
from bs4 import BeautifulSoup

url = "https://ge.globo.com/?utm_source=globo.com&utm_medium=menuburger"

resposta = requests.get(url)
if resposta.status_code == 200:
    soup = BeautifulSoup(resposta.content, 'html.parser')

    noticias = soup.find_all('a', class_='feed-post-link gui-color-primary gui-color-hover')

    for noticia in noticias:
        titulo = noticia.find('p').text
        print(f'Noticia: {titulo}')

else:
    print(f"Erro ao acessar a página. {resposta.status_code}")