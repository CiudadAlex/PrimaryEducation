from ai.llm.LLM import LLM
from util.RandomLineLoader import RandomLineLoader
from constants.Constants import Constants


class SpanishStartReadingTask:

    @staticmethod
    def execute(number_of_words=10):

        # llm = LLM(model="ai/llama3.1:8B-Q4_K_M")
        # llm.execute("hola como estas?")

        list_random_words = RandomLineLoader.get_random_words(Constants.CORPUS_SPANISH_BASIC_WORDS, number_of_lines=number_of_words)
        print(list_random_words)

