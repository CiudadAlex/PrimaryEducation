from ai.llm.LLM import LLM
from util.RandomWordLoader import RandomWordLoader

# llm = LLM(model="ai/llama3.1:8B-Q4_K_M")
# llm.execute("hola como estas?")

RandomWordLoader.get_random_words("./corpus/SpanishBasicWords.txt", 10)
