# Olha Svezhentseva
# 01.09.2022
from typing import Tuple, Union
from nltk import word_tokenize

from .bksearch import BKSearcher


class Chat:
    "A class responsible for communication with the user."

    WARNINGS = {
        "invalid length": "Input must be in the following format: word number. Try again.",
        "invalid word": "Your input must begin with a string. Try again.",
        "invalid distance": "After a word there must be a number. Try again."
    }

    def __init__(self, searcher: BKSearcher):
        self.searcher = searcher

    def _show_warning_message(self, status: str) -> str:
        """The method prints a warning to the user."""
        return self.WARNINGS[status]

    def run_interactive_mode(self) -> None:
        """
        The method is responsible for continuous flow of the program,
        so that user's input is always awaited.
        """
        print(f"The program will now switch to interactive mode. "
              "Empty input will stop the program.")
        while True:
            print(f"Type a word and the maximum distance a string can be from your word "
                  "and will still be returned. "
                  "There must be a space between the word and the number.")
            user_input = input().strip().lower()
            if user_input == "":
                print("Bye!")
                break
            status, *result = self._check_input(user_input)
            if status:
                print(f"Results: {self.searcher.execute_command(result[0], result[1])}")
            else:
                print(self._show_warning_message(result[0]))

    def _check_input(self, user_input: str) -> Union[str, Tuple]:
        """The method processes user's input. """
        user_input = word_tokenize(user_input)
        if not self._valid_length(user_input):
            return False, "invalid length"

        word = user_input[0]
        d = user_input[1]

        if not self._not_number(word):
            return False, "invalid word"

        if not self._valid_distance(d):
            return False, "invalid distance"
        return True, word, d

    @staticmethod
    def _valid_length(query: str) -> bool:
        """The method checks input's length."""
        return len(query) == 2

    @staticmethod
    def _not_number(word: str) -> bool:
        """The method checks that a word doesn't solely consist of numbers."""
        try:
            int(word)
        except ValueError:
            return True
        return False

    @staticmethod
    def _valid_distance(d) -> bool:
        """The method checks that distance can be converted to a float."""
        try:
            float(d)
        except ValueError:
            return False
        return True

