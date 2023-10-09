from FilePy.Board import Board
from FilePy.RevealedElement import RevealedElement


class Player:
    def __init__(self, name: str, board: Board, color: str) -> None:
        self.__name_gamer__: str = name
        self.__board__: Board = board
        self.__punctuation__: int = 0
        self.__color__: str = color

        self.__current_guess__: tuple[str, int] = tuple()
        self.__bigger_guess_list__: list[tuple[str, int, str]] = []
        self.__minor_guess_list__: list[tuple[str, int, str]] = []
        self.__equal_guess_list__: list[tuple[str, int, str]] = []

    def set_current_guess(self, current_guess: tuple[str, int]) -> None:
        self.__current_guess__ = current_guess

    def add_history(self):
        coord, number = self.__current_guess__
        guess: tuple[str, int, str] = (coord, number, self.__color__)

        if self.is_max():
            self.__bigger_guess_list__.append(guess)
        elif self.is_min():
            self.__minor_guess_list__.append(guess)
        else:
            self.__equal_guess_list__.append(guess)

    def count_points(self) -> None:
        RIGHT_GUESS: int = 0

        if self.get_difference_of_guess_to_sum() == RIGHT_GUESS:
            self.__punctuation__ += self.__board__.count_revealed_houses(self.__current_guess__)
        elif not self.__board__.is_coordinate_complete(self.__current_guess__):
            self.__punctuation__ += 1

    def get_difference_of_guess_to_sum(self) -> int:
        if self.__current_guess__[1] < self.__board__.get_sum_of_coordinate(self.__current_guess__):
            return self.__board__.get_sum_of_coordinate(self.__current_guess__) - self.__current_guess__[1]

        return self.__current_guess__[1] - self.__board__.get_sum_of_coordinate(self.__current_guess__)

    def reveal_house(self) -> list[RevealedElement]:
        if self.is_max() and not self.__board__.is_coordinate_complete(self.__current_guess__):
            return self.__board__.get_reveal_max(self.__current_guess__, self.__color__)

        elif self.is_min() and not self.__board__.is_coordinate_complete(self.__current_guess__):
            return self.__board__.get_reveal_min(self.__current_guess__, self.__color__)

        elif not self.__board__.is_coordinate_complete(self.__current_guess__):
            return self.__board__.get_reveal_all(self.__current_guess__, self.__color__)

        return []

    def is_max(self):
        if self.__current_guess__[1] <= self.__board__.get_sum_of_coordinate(self.__current_guess__):
            return False
        return True

    def is_min(self):
        if self.__current_guess__[1] >= self.__board__.get_sum_of_coordinate(self.__current_guess__):
            return False
        return True

    def get_board(self) -> Board:
        return self.__board__

    def get_name(self) -> str:
        return self.__name_gamer__

    def get_punctuation(self) -> int:
        return self.__punctuation__

    def get_history_guess_max(self) -> list[tuple[str, int, str]]:
        return self.__bigger_guess_list__

    def get_history_guess_min(self) -> list[tuple[str, int, str]]:
        return self.__minor_guess_list__

    def get_history_guess_eguais(self) -> list[tuple[str, int, str]]:
        return self.__equal_guess_list__
