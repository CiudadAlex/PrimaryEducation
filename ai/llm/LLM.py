import subprocess

"""
Caller for an LLM. Example call:

docker model run ai/llama3.1:8B-Q4_K_M "what is a black hole"
"""


class LLM:

    def __init__(self, model="ai/llama3.1:8B-Q4_K_M"):
        self.model = model

    def execute(self, text):
        # Ejecutar el comando y capturar la salida
        resultado = subprocess.run(['docker', 'model', 'run', self.model, text], capture_output=True, text=True)

        # Mostrar la salida estándar
        print("Salida estándar:")
        print(resultado.stdout)

        # Mostrar errores (si hay)

        print("Errores:")
        print(resultado.stderr)



