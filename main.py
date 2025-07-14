import requests
from bs4 import BeautifulSoup


def extraer_tags_con_propiedad(url, propiedad):
    # 1. Descargar el contenido HTML de la URL
    respuesta = requests.get(url)

    if respuesta.status_code != 200:
        print(f"Error al acceder a la URL: {respuesta.status_code}")
        return []

    # 2. Analizar el HTML con BeautifulSoup
    soup = BeautifulSoup(respuesta.text, 'html.parser')

    # 3. Buscar todas las etiquetas que contienen la propiedad especificada
    contenido = soup.find(id="bodyContent")


    return contenido


# Ejemplo de uso
url = 'https://es.wiktionary.org/wiki/Ap%C3%A9ndice:1000_palabras_b%C3%A1sicas_en_espa%C3%B1ol'
propiedad = 'data-role'

tags_con_propiedad = extraer_tags_con_propiedad(url, propiedad)

# Mostrar los resultados
for tag in tags_con_propiedad:
    print(tag)
