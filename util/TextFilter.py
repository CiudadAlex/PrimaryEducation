

class TextFilter:

    @staticmethod
    def remove_of_list_if_item_contains(list_text, contained_in_item):

        list_text_return = []

        for text in list_text:
            if contained_in_item not in text:
                list_text_return.append(text.strip())

        return list_text_return

    @staticmethod
    def truncate_text_of_list(list_text, final_char_seq):

        list_text_return = []

        for text in list_text:

            index = text.find(final_char_seq)

            if index != -1:
                truncated_text = text[:index]
            else:
                truncated_text = text

            list_text_return.append(truncated_text.strip())

        return list_text_return

    @staticmethod
    def remove_of_list_if_text_is_short(list_text, min_number_chars):

        list_text_return = []

        for text in list_text:
            if len(text) >= min_number_chars:
                list_text_return.append(text)

        return list_text_return

