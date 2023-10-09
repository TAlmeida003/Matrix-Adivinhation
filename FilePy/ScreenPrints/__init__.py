import os

from FilePy.HiddenSums import HiddenSums
from FilePy.RevealedElement import RevealedElement


def get_report_error(text: str) -> None:
    SIZE_CENTER_TEXT: int = 170
    NUM_BAR: int = 40

    print(get_paint_color("RED"), ('=-' * NUM_BAR).center(SIZE_CENTER_TEXT))
    print("ERRO!!!".center(SIZE_CENTER_TEXT + 1))
    print(text.center(SIZE_CENTER_TEXT))
    print(('=-' * NUM_BAR).center(SIZE_CENTER_TEXT + 3), get_paint_color())


def get_clear_prompt() -> None:
    if os.name == 'nt':
        os.system('cls') or None
    else:
        os.system('clear') or None


def display_sub_title(text: str) -> None:
    SIZE_CENTER_TEXT: int = 170
    NUM_BAR: int = 40

    print(get_paint_color("BLUE"))
    print(("=-" * NUM_BAR).center(SIZE_CENTER_TEXT + 2, " "))
    print(text.center(SIZE_CENTER_TEXT - 4))
    print(("=-" * NUM_BAR).center(SIZE_CENTER_TEXT + 2, " "))
    print(get_paint_color())


def display_header(text: str) -> None:
    SIZE_CENTER_TEXT: int = 170

    display_sub_title("SOMAS ESCONDIDAS")

    print(("= " * 23).center(SIZE_CENTER_TEXT - 2, " "))
    print((("==" * 10) + get_paint_color("BLUE") + " " + text + " "
           + get_paint_color() + ("==" * 10)).center(SIZE_CENTER_TEXT + 11))
    print(("= " * 20).center(SIZE_CENTER_TEXT, " "))
    print(("= " * 15).center(SIZE_CENTER_TEXT, " "))
    print(("= " * 5).center(SIZE_CENTER_TEXT, " "))
    print(("= " * 3).center(SIZE_CENTER_TEXT, " "))


def get_baseboard() -> None:
    SIZE_CENTER: int = 170

    print("\n")
    print(("-=" * 40).center(SIZE_CENTER))


def get_paint_color(color: str = "WHITE") -> str:
    dict_color: dict[str, str] = {"RED": "\033[1;31m", "BLUE": "\033[1;34m", "YELLOW": "\033[1;33m",
                                  "GREEN": "\033[1;32m"}
    if color in dict_color:
        return dict_color[color]

    return "\033[1;97m"


def get_display_option(color: str, num_option: str, name_option: str) -> None:
    SIZE_CENTER_TEXT: int = 170

    print(get_paint_color(color))
    print("\n", f"[ {num_option} ] — {name_option}".center(SIZE_CENTER_TEXT))
    print(get_paint_color())


def display_array(hiddenSums: HiddenSums) -> None:
    dict_column_coordinates: dict[str, list[str]] = {"EASY": [" ", "C0", "C1", "C2", "SOMA"],
                                                     "AVERAGE": [" ", "C0", "C1", "C2", "C3", "SOMA"],
                                                     "DIFFICULT": [" ", "C0", "C1", "C2", "C3", "C4", "SOMA"]
                                                     }
    dict_line_coordinates: dict[str, list[str]] = {"EASY": ["L0", "L1", "L2", "SOMA"],
                                                   "AVERAGE": ["L0", "L1", "L2", "L3", "SOMA"],
                                                   "DIFFICULT": ["L0", "L1", "L2", "L3", "L4", "SOMA"]
                                                   }
    dict_range: dict[str, int] = {"EASY": 3, "AVERAGE": 4, "DIFFICULT": 5}
    dict_print: dict[str, int] = {"EASY": 225, "AVERAGE": 240, "DIFFICULT": 254}

    line = 0
    SIZE_CENTER: int = 170

    print(("|T" + "======T" * len(dict_column_coordinates[hiddenSums.get_level()]) + "|").center(SIZE_CENTER))
    print(("|" + "------|" * len(dict_column_coordinates[hiddenSums.get_level()])).center(SIZE_CENTER))

    string: str = "|"
    for i in dict_column_coordinates[hiddenSums.get_level()]:
        string += f'{i:^6}'"|"
    print(string.center(SIZE_CENTER))

    print(("|" + "------|" * len(dict_column_coordinates[hiddenSums.get_level()])).center(SIZE_CENTER))

    for i in dict_line_coordinates[hiddenSums.get_level()]:
        string = ""
        string += f"|{i:^6}|"
        for column in range(dict_range[hiddenSums.get_level()] + 1):
            array: list[list[RevealedElement]] = hiddenSums.get_current_player().get_board().get_revealed_int_array()

            string += f'{array[line][column].get_str():^20}' + "|"
        line += 1

        print(string.center(dict_print[hiddenSums.get_level()]))
        print(("|" + "------|" * len(dict_column_coordinates[hiddenSums.get_level()])).center(SIZE_CENTER))

    print(("|T" + "======T" * len(dict_column_coordinates[hiddenSums.get_level()]) + "|").center(SIZE_CENTER))


def display_history(hiddenSums: HiddenSums) -> None:
    STR_GUESS_MAX: str = "PALPITES MAIORES:"
    list_max: list[tuple[str, int, str]] = join_list(hiddenSums.get_player_one().get_history_guess_max(),
                                                     hiddenSums.get_player_two().get_history_guess_max())
    STR_GUESS_MIN: str = "PALPITES MENORES:"
    list_min: list[tuple[str, int, str]] = join_list(hiddenSums.get_player_one().get_history_guess_min(),
                                                     hiddenSums.get_player_two().get_history_guess_min())
    STR_GUESS_EGUAIS: str = "PALPITES IGUAIS:"
    list_eguais: list[tuple[str, int, str]] = join_list(hiddenSums.get_player_one().get_history_guess_eguais(),
                                                        hiddenSums.get_player_two().get_history_guess_eguais())

    print()
    list_history(STR_GUESS_MIN, list_min)
    list_history(STR_GUESS_MAX, list_max)
    list_history(STR_GUESS_EGUAIS, list_eguais)


def join_list(list1: list[tuple[str, int, str]], list2: [tuple[str, int, str]]):
    n1 = len(list1)
    n2 = len(list2)
    list_final = []
    tam_max = max(n1, n2)

    for i in range(tam_max):
        if i < n1:
            list_final.append(list1[i])
        if i < n2:
            list_final.append(list2[i])

    return list_final


def list_history(string: str, list_h: [tuple[str, int, str]]) -> None:
    string += " "
    PAINT_WHITE: str = "\033[1;97m"
    for i in range(len(list_h)):
        string += f"|{list_h[i][2]}{list_h[i][0]} : {list_h[i][1]}{PAINT_WHITE}| "

    print(" " * 46, end="")
    print(string)


def display_winner(hiddenSums: HiddenSums) -> None:
    display_header(hiddenSums.decide_winner())
    print()
    print(("MODO DE JOGO: " + get_paint_color("BLUE")
           + hiddenSums.get_level()
           + get_paint_color()).center(125))
    print(("STATUS: " + get_paint_color("YELLOW")
           + " " * 5 + f"{hiddenSums.get_player_one().get_name()}: |{hiddenSums.get_player_one().get_punctuation():^5}|"
           + get_paint_color()
           + get_paint_color("RED")
           + " " * 5 + f"{hiddenSums.get_player_two().get_name()}: |{hiddenSums.get_player_two().get_punctuation():^5}|"
           + get_paint_color()
           + " " * 5 + f"Rodada: |{hiddenSums.get_current_round() :^5}|").center(200))
    display_array(hiddenSums)
    display_history(hiddenSums)
    get_baseboard()

    input(" Pressione [ENTER] para retorna para o menu principal ".center(170, "-"))
    get_clear_prompt()
