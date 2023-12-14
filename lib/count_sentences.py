#!/usr/bin/env python3

class MyString:
    def __init__(self, value=None):
        if value is None:
            print("The value must be a string.")
        else:
            self.set_value(value)

    def get_value(self):
        return self._value

    def set_value(self, new_value):
        if not isinstance(new_value, str) or not new_value:
            print("The value must be a non-empty string.")
        else:
            self._value = new_value

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        if not hasattr(self, '_value'):
            print("The value must be set before counting sentences.")
            return 0

        cleaned_value = self._value.replace('?', '.').replace('!', '.')
        sentences = [sentence.strip() for sentence in cleaned_value.split('.') if sentence.strip()]
        return len(sentences)


