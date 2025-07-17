from util.HtmlCrawler import HtmlCrawler
from util.TextFilter import TextFilter
from util.FileBuilder import FileBuilder
from constants.Constants import Constants


class SpanishBasicWordsCrawler:

    @staticmethod
    def execute():

        url = 'https://es.wiktionary.org/wiki/Ap%C3%A9ndice:1000_palabras_b%C3%A1sicas_en_espa%C3%B1ol'

        soup = HtmlCrawler.get_soup_handle(url)
        html_tag = soup.find(id="bodyContent")
        html_tag = html_tag.find(id="mw-content-text")

        sections = html_tag.find_all('section')
        sections = sections[1:]

        list_lines = []

        for s in sections:
            lines_section = s.text.splitlines()
            for line in lines_section:
                list_lines.append(line)

        print(f"list_lines: {len(list_lines)}")

        list_lines = TextFilter.remove_of_list_if_item_contains(list_lines, "[editar]")

        print(f"list_lines: {len(list_lines)}")

        list_lines = TextFilter.truncate_text_of_list(list_lines, ",")

        print(f"list_lines: {len(list_lines)}")

        list_lines = TextFilter.remove_of_list_if_text_is_short(list_lines, 5)

        print(f"list_lines: {len(list_lines)}")

        list_lines = TextFilter.remove_of_list_if_item_contains(list_lines, " ")

        print(f"list_lines: {len(list_lines)}")

        file_builder = FileBuilder(Constants.CORPUS_SPANISH_BASIC_WORDS)
        for line in list_lines:
            file_builder.append(line + "\n")

        file_builder.write_to_disk()



