

class TextFilter:

    @staticmethod
    def remove_of_list_if_item_contains(list_text, contained_in_item):

        list_text_return = []

        for text in list_text:
            if contained_in_item not in text:
                list_text_return.append(text)

        return list_text_return


