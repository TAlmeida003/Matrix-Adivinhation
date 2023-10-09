from FilePy.HiddenSums import HiddenSums
from FilePy.Inputs import LevelMenu, BoardNumberMenu, NumberOfRoundsMenu, PlayerMovement
from FilePy import ScreenPrints


def player_movement(hiddenSums: HiddenSums) -> None:
    coordinates: str
    guess: int

    coordinates, guess = PlayerMovement.inicialize(hiddenSums)
    hiddenSums.add_guess((coordinates, guess))
    hiddenSums.next_player()


def register_settings() -> HiddenSums:
    level: str = LevelMenu.inicialize()
    number_of_board: int = BoardNumberMenu.inicialize()
    number_of_rounds: int = NumberOfRoundsMenu.inicialize(level)

    return HiddenSums(number_of_rounds, number_of_board, level)


def decide_winner(hiddenSums: HiddenSums) -> None:
    ScreenPrints.display_winner(hiddenSums)


def inicialize() -> None:
    hiddenSums: HiddenSums = register_settings()

    while not hiddenSums.is_number_matches_are_over() and not hiddenSums.is_board_complete():
        player_movement(hiddenSums)
        player_movement(hiddenSums)

        hiddenSums.add_history_player()
        hiddenSums.to_score()
        hiddenSums.reveal_winner_coordinates()
        hiddenSums.next_round()

    decide_winner(hiddenSums)
