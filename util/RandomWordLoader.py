import random


class RandomWordLoader:

    @staticmethod
    def get_random_words(file_path, number_of_words):

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            if len(lines) >= number_of_words:
                random_lines = random.sample(lines, number_of_words)
            else:
                random_lines = lines

            for line in random_lines:
                print(line.strip())

        except FileNotFoundError:
            print(f"❌ The file '{file_path}' was not found.")
        except Exception as e:
            print(f"⚠️ Error reading the file: {e}")
