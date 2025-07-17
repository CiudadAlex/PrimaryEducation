

class FileBuilder:

    def __init__(self, file_path):
        self.file_path = file_path
        self.content = ""

    def append(self, text):
        self.content = self.content + text

    def write_to_disk(self):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write(self.content)

