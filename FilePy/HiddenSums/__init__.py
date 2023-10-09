from FilePy.Board import Board
from FilePy.Player import Player
from FilePy.RevealedElement import RevealedElement
from FilePy import ScreenPrints


class HiddenSums:
    def __init__(self, number_of_rounds: int, number_of_board: int, level: str) -> None:

        self.__level__: str = level
        self.__number_of_rounds__: int = number_of_rounds
        self.__number_of_board__ = number_of_board
        self.__number_current_of_rounds__: int = 1

        board_player_1, board_player_2 = self.create_player()
        self.__player_one__: Player = Player("Jogador Nº1", board_player_1, ScreenPrints.get_paint_color("YELLOW"))
        self.__player_two__: Player = Player("Jogador Nº2", board_player_2, ScreenPrints.get_paint_color("RED"))
        self.__current_player__: Player = self.__player_one__

    def create_player(self) -> tuple[Board, Board]:
        if self.__number_of_board__ == 1:
            board_player: Board = Board(self.__level__)
            return board_player, board_player

        board_player_1: Board = Board(self.__level__)
        board_player_2: Board = Board(self.__level__)
        return board_player_1, board_player_2

    def add_history_player(self) -> None:
        self.__player_one__.add_history()
        self.__player_two__.add_history()

    def is_number_matches_are_over(self) -> bool:
        return self.__number_current_of_rounds__ > self.__number_of_rounds__

    def is_coordinate_complete(self, coordinate: tuple[str, int]) -> bool:
        return self.__current_player__.get_board().is_coordinate_complete(coordinate)

    def to_score(self) -> None:
        GUSS_PLAYER_ONE: int = self.__player_one__.get_difference_of_guess_to_sum()
        GUSS_PLAYER_TWO: int = self.__player_two__.get_difference_of_guess_to_sum()

        if GUSS_PLAYER_ONE < GUSS_PLAYER_TWO:
            self.__player_one__.count_points()
        elif GUSS_PLAYER_ONE > GUSS_PLAYER_TWO:
            self.__player_two__.count_points()
        else:
            self.__player_one__.count_points()
            self.__player_two__.count_points()

    def get_current_player(self) -> Player:
        return self.__current_player__

    def add_guess(self, coordinate: tuple[str, int]) -> None:
        self.__current_player__.set_current_guess(coordinate)

    def next_player(self) -> None:
        if self.__current_player__ is self.__player_one__:
            self.__current_player__ = self.__player_two__
        else:
            self.__current_player__ = self.__player_one__

    def reveal_winner_coordinates(self) -> None:
        GUSS_PLAYER_ONE: int = self.__player_one__.get_difference_of_guess_to_sum()
        GUSS_PLAYER_TWO: int = self.__player_two__.get_difference_of_guess_to_sum()

        if GUSS_PLAYER_ONE < GUSS_PLAYER_TWO:
            list_elements: list[RevealedElement] = self.__player_one__.reveal_house()
            self.__player_one__.get_board().add_relevant_elements(list_elements)
        elif GUSS_PLAYER_ONE > GUSS_PLAYER_TWO:
            list_elements: list[RevealedElement] = self.__player_two__.reveal_house()
            self.__player_two__.get_board().add_relevant_elements(list_elements)
        else:
            list_elements_one: list[RevealedElement] = self.__player_one__.reveal_house()
            list_elements_two: list[RevealedElement] = self.__player_two__.reveal_house()
            self.reveal_tie(list_elements_one, list_elements_two)

    def reveal_tie(self, list_elements_one: list[RevealedElement], list_elements_two: list[RevealedElement]) -> None:
        if self.__number_of_board__ == 1:
            self.join_list(list_elements_one, list_elements_two)
        else:
            self.__player_one__.get_board().add_relevant_elements(list_elements_one)
            self.__player_two__.get_board().add_relevant_elements(list_elements_two)

    def join_list(self, list_elements_one: list[RevealedElement], list_elements_two: list[RevealedElement]) -> None:
        for element in list_elements_one:
            if not element.in_list(list_elements_two):
                list_elements_two.append(element)
            else:
                INDEX: int = element.index_list(list_elements_two)
                list_elements_two[INDEX].set_color("\033[1;97m")
        self.__player_one__.get_board().add_relevant_elements(list_elements_two)

    def next_round(self) -> None:
        self.__number_current_of_rounds__ += 1

    def get_player_one(self) -> Player:
        return self.__player_one__

    def get_player_two(self) -> Player:
        return self.__player_two__

    def is_board_complete(self) -> bool:
        IS_BOARD_COMPLETE_PLAYER_ONE: bool = self.__player_one__.get_board().is_board_complete()
        IS_BOARD_COMPLETE_PLAYER_TWO: bool = self.__player_two__.get_board().is_board_complete()

        return IS_BOARD_COMPLETE_PLAYER_ONE or IS_BOARD_COMPLETE_PLAYER_TWO

    def get_level(self) -> str:
        return self.__level__

    def get_current_round(self) -> int:
        return self.__number_current_of_rounds__

    def decide_winner(self) -> str:
        if self.__player_one__.get_punctuation() > self.__player_two__.get_punctuation():
            return "Vencedor" + self.__player_one__.get_name()
        elif self.__player_one__.get_punctuation() < self.__player_two__.get_punctuation():
            return "Vencedor" + self.__player_two__.get_name()

        return "Empate"
