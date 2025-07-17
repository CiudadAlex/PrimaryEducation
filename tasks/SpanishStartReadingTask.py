from ai.llm.LLM import LLM
from util.RandomLineLoader import RandomLineLoader
from constants.Constants import Constants


class SpanishStartReadingTask:

    def __init__(self):
        self.llm = LLM(model="ai/llama3.1:8B-Q4_K_M")

    def execute(self, number_of_words=10):

        list_random_words = RandomLineLoader.get_random_words(Constants.CORPUS_SPANISH_BASIC_WORDS, number_of_lines=number_of_words)
        print(list_random_words)

        response = self.llm.execute("hola como estas?")
        print(response)

