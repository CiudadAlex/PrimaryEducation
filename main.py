from ai.llm.LLM import LLM
from util.RandomLineLoader import RandomLineLoader
from constants.Constants import Constants

# llm = LLM(model="ai/llama3.1:8B-Q4_K_M")
# llm.execute("hola como estas?")

RandomLineLoader.get_random_words(Constants.CORPUS_SPANISH_BASIC_WORDS, 10)
