from ai.llm.LLM import LLM
from util.RandomLineLoader import RandomLineLoader
from constants.Constants import Constants


class SpanishStartReadingTask:

    def __init__(self):
        self.llm = LLM(model="ai/llama3.1:8B-Q4_K_M")

    def execute(self, number_of_words=10):

        list_random_words = RandomLineLoader.get_random_words(Constants.CORPUS_SPANISH_BASIC_WORDS, number_of_lines=number_of_words)
        self.print_in_log("WORDS", list_random_words)

        partition_words = SpanishStartReadingTask.partition_list(list_random_words, 3)

        for list_words in partition_words:
            response = self.call_llm(list_words)
            self.print_in_log("RESPONSE", response)

    def call_llm(self, list_words):

        prompt = "Crea una frase no muy larga usando lenguaje sencillo que puedan entender un niño de primaria y en la que uses las palabras:"

        for word in list_words:
            prompt = prompt + " '" + word + "',"

        self.print_in_log("PROMPT", prompt)

        response = self.llm.execute(prompt)

        return response

    def print_in_log(self, title, obj):
        print("#####################")
        print(title)
        print(obj)
        print("#####################")

    @staticmethod
    def partition_list(list_obj, size):
        return [list_obj[i:i + size] for i in range(0, len(list_obj), size)]

