from util.HtmlCrawler import HtmlCrawler

url = 'https://es.wiktionary.org/wiki/Ap%C3%A9ndice:1000_palabras_b%C3%A1sicas_en_espa%C3%B1ol'

soup = HtmlCrawler.get_soup_handle(url)
tags_con_propiedad = soup.find(id="bodyContent")

# Mostrar los resultados
for tag in tags_con_propiedad:
    print(tag)
