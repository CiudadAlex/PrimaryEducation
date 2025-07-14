from util.HtmlCrawler import HtmlCrawler

url = 'https://es.wiktionary.org/wiki/Ap%C3%A9ndice:1000_palabras_b%C3%A1sicas_en_espa%C3%B1ol'

soup = HtmlCrawler.get_soup_handle(url)
html_tag = soup.find(id="bodyContent")
html_tag = html_tag.find(id="mw-content-text")

sections = html_tag.find_all('section')

list_ul = []

for s in sections:
    ul = s.find_all('ul')
    if len(ul) > 0:
        list_ul.append(ul)

for ul in list_ul:
    print("###############################################")
    print(str(ul))
    print("###############################################")

