import random


class RandomLineLoader:

    @staticmethod
    def get_random_words(file_path, number_of_lines):

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            if len(lines) >= number_of_lines:
                random_lines = random.sample(lines, number_of_lines)
            else:
                random_lines = lines

            return random_lines

        except FileNotFoundError:
            print(f"❌ The file '{file_path}' was not found.")
        except Exception as e:
            print(f"⚠️ Error reading the file: {e}")
