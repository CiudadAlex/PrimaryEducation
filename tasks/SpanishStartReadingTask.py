from ai.llm.LLM import LLM
from util.RandomLineLoader import RandomLineLoader
from constants.Constants import Constants
from util.FileBuilder import FileBuilder
from datetime import datetime
import random


class SpanishStartReadingTask:

    def __init__(self):

        str_now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        self.llm = LLM(model="ai/llama3.1:8B-Q4_K_M")
        self.file_builder = FileBuilder(Constants.OUTPUT_DIR + "SpanishStartReadingTask_" + str_now + ".txt")

    def execute(self, number_of_words=12, iterations=3):

        list_random_words = self.complete_list_random_words(number_of_words, [])

        for i in range(iterations):
            self.append_to_file_list_of_words_and_phrases(list_random_words)
            sample_of_previous_words = random.sample(list_random_words, int(number_of_words / 2))
            list_random_words = self.complete_list_random_words(number_of_words, sample_of_previous_words)

        self.file_builder.write_to_disk()

    def complete_list_random_words(self, number_of_words, list_previous_words):

        needed_number_of_words = number_of_words - len(list_previous_words)
        list_new_random_words = RandomLineLoader.get_random_words(Constants.CORPUS_SPANISH_BASIC_WORDS, number_of_lines=needed_number_of_words)
        completed_list = list_previous_words + list_new_random_words

        random.shuffle(completed_list)
        return completed_list

    def append_to_file_list_of_words_and_phrases(self, list_of_words):

        words_for_file = ", ".join(list_of_words)
        self.file_builder.append("Palabras:\n")
        self.file_builder.append(words_for_file + "\n\n")
        self.print_in_log("WORDS", list_of_words)

        self.file_builder.append("Frases:\n")

        partition_words = SpanishStartReadingTask.partition_list(list_of_words, 3)

        for list_words in partition_words:
            response = self.call_llm(list_words)
            self.file_builder.append(response + "\n")
            self.print_in_log("RESPONSE", response)

        self.file_builder.append("############################################\n\n")

    def call_llm(self, list_words):

        prompt = "Crea una frase lo más corta posible usando lenguaje sencillo que pueda entender un niño de primaria y en la que uses las palabras exactas:"

        for word in list_words:
            prompt = prompt + " '" + word + "',"

        self.print_in_log("PROMPT", prompt)

        response = self.llm.execute(prompt)
        response = response.replace('"', '')

        return response

    def print_in_log(self, title, obj):
        print("#####################")
        print(title)
        print(obj)
        print("#####################")

    @staticmethod
    def partition_list(list_obj, size):
        return [list_obj[i:i + size] for i in range(0, len(list_obj), size)]

