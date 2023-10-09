from FilePy import ScreenPrints
from FilePy.HiddenSums import HiddenSums


def check_coordinate(coordinates: str, hiddenSums: HiddenSums) -> None:
    dict_coord = {"EASY": {"C0", "C1", "C2", "L0", "L1", "L2"},
                  "AVERAGE": {"C0", "C1", "C2", "C3", "L0", "L1", "L2", "L3"},
                  "DIFFICULT": {"C0", "C1", "C2", "C3", "C4", "L0", "L1", "L2", "L3", "L4"}
                  }
    if coordinates not in dict_coord[hiddenSums.get_level()]:
        raise RuntimeError("A coordenada informada não faz parte do tabuleiro")
    elif hiddenSums.is_coordinate_complete((coordinates, 0)):
        raise RuntimeError("A coordenada informada já etá completa")


def is_valid_coordinates(coordinates: str, hiddenSums: HiddenSums) -> bool:
    try:
        check_coordinate(coordinates, hiddenSums)
        return True
    except RuntimeError as error:
        ScreenPrints.get_report_error(error.__str__())
        return False


def check_guess(hiddenSums: HiddenSums, guess: int) -> None:
    dict_limit_min: dict[str, int] = {"EASY": 6, "AVERAGE": 10, "DIFFICULT": 15}
    dict_limit_max: dict[str, int] = {"EASY": 87, "AVERAGE": 234, "DIFFICULT": 490}

    if dict_limit_min[hiddenSums.get_level()] > guess or guess > dict_limit_max[hiddenSums.get_level()]:
        raise RuntimeError(f"O palpite está fora no limite, seu palpite deve está entre "
                           f"{dict_limit_min[hiddenSums.get_level()]} até {dict_limit_max[hiddenSums.get_level()]}")


def is_valid_guess(hiddenSums: HiddenSums, guess: int) -> bool:
    try:
        check_guess(hiddenSums, guess)
        return True
    except RuntimeError as error:
        ScreenPrints.get_report_error(error.__str__())
        return False


def display(hiddenSums: HiddenSums) -> None:
    ScreenPrints.display_header(f"TABULEIRO {hiddenSums.get_current_player().get_name().upper()}")
    print()
    print(("MODO DE JOGO: " + ScreenPrints.get_paint_color("BLUE")
           + hiddenSums.get_level()
           + ScreenPrints.get_paint_color()).center(125))
    print(("STATUS: " + ScreenPrints.get_paint_color("YELLOW")
           + " " * 5 + f"{hiddenSums.get_player_one().get_name()}: |{hiddenSums.get_player_one().get_punctuation():^5}|"
           + ScreenPrints.get_paint_color()
           + ScreenPrints.get_paint_color("RED")
           + " " * 5 + f"{hiddenSums.get_player_two().get_name()}: |{hiddenSums.get_player_two().get_punctuation():^5}|"
           + ScreenPrints.get_paint_color()
           + " " * 5 + f"Rodada: |{hiddenSums.get_current_round() :^5}|").center(200))

    print()
    ScreenPrints.display_array(hiddenSums)
    ScreenPrints.display_history(hiddenSums)
    print()
    print(("-=" * 40).center(170))
    print(" " * 50, end="* ")


def input_coordinates(hiddenSums: HiddenSums) -> str:
    display(hiddenSums)
    coordinates: str = input("INFORME A COORDENADA DESEJADA: ").upper()

    return coordinates


def input_guess() -> int:
    try:
        print(" " * 50, end="* ")
        guess: int = int(input("INFORME O PALPITE DESEJADO: "))
        ScreenPrints.get_clear_prompt()
        return guess
    except ValueError:
        ScreenPrints.get_clear_prompt()
        return -1


def inicialize(hiddenSums: HiddenSums) -> tuple[str, int]:
    coordinates: str = input_coordinates(hiddenSums)
    guess: int = input_guess()

    while not (is_valid_coordinates(coordinates, hiddenSums) and is_valid_guess(hiddenSums, guess)):
        coordinates: str = input_coordinates(hiddenSums)
        guess: int = input_guess()

    return coordinates, guess

