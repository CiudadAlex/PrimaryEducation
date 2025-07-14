import requests
from bs4 import BeautifulSoup


class HtmlCrawler:

    @staticmethod
    def get_soup_handle(url):

        html_response = requests.get(url)

        if html_response.status_code != 200:
            print(f"Error {html_response.status_code} getting URL: {url}")
            return []

        soup = BeautifulSoup(html_response.text, 'html.parser')

        return soup
