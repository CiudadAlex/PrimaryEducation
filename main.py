from ai.llm.LLM import LLM

llm = LLM(model="ai/llama3.1:8B-Q4_K_M")
llm.execute("hola como estas?")

