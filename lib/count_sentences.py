import re
import io
import sys

class MyString:
    """
    MyString class represents a string with additional methods for sentence analysis.
    """

    def __init__(self, value=""):
        """
        Initialize the MyString instance.

        Args:
            value (str): The string value.
        """
        if not isinstance(value, str):
            raise ValueError("The value must be a string.")
        self.value = value

    def is_sentence(self):
        """
        Check if the value ends with a period.

        Returns:
            bool: True if the value ends with a period, False otherwise.
        """
        return self.value.endswith('.')

    def is_question(self):
        """
        Check if the value ends with a question mark.

        Returns:
            bool: True if the value ends with a question mark, False otherwise.
        """
        return self.value.endswith('?')

    def is_exclamation(self):
        """
        Check if the value ends with an exclamation mark.

        Returns:
            bool: True if the value ends with an exclamation mark, False otherwise.
        """
        return self.value.endswith('!')

    def count_sentences(self):
        """
        Count the number of sentences in the value.

        Returns:
            int: The number of sentences.
        """
        sentences = [s.strip() for s in re.split(r'[.!?]', self.value) if s.strip()]
        return len(sentences)


string = MyString("This is a string! It has three sentences. Right?")
print(string.is_sentence())    
print(string.is_question())    
print(string.is_exclamation())  
print(string.count_sentences()) 

class TestMyString:
    def test_value_string(self):
        '''prints "The value must be a string." if not string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        try:
            string = MyString(123)
        except ValueError as e:
            print(e)
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "The value must be a string.\n"


test = TestMyString()
test.test_value_string()
