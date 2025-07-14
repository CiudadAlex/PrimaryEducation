from util.HtmlCrawler import HtmlCrawler

url = 'https://es.wiktionary.org/wiki/Ap%C3%A9ndice:1000_palabras_b%C3%A1sicas_en_espa%C3%B1ol'

soup = HtmlCrawler.get_soup_handle(url)
html_tag = soup.find(id="bodyContent")
html_tag = html_tag.find(id="mw-content-text")

sections = html_tag.find_all('section')

for s in sections:
    print(s.text)

