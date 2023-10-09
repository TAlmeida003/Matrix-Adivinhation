from FilePy import ScreenPrints


def convert_option_in_level(user_choice: str) -> str:
    list_level: list[str] = ["EASY", "AVERAGE", "DIFFICULT"]
    return list_level[int(user_choice) - 1]


def check_level(user_choice: str) -> None:
    set_option: set[str] = {"1", "2", "3"}

    if user_choice not in set_option:
        raise RuntimeError("O NÍVEL INFORMADO NÃO ESTÁ DISPONÍVEL")


def is_valid_level(user_choice: str) -> bool:
    try:
        check_level(user_choice)
        return True
    except RuntimeError as error:
        ScreenPrints.get_report_error(error.__str__())
        return False


def display_option_level() -> None:
    ScreenPrints.get_display_option("WHITE", "1", "FÁCIL - TABULEIRO 3 X 3")
    ScreenPrints.get_display_option("BLUE", "2", "MÉDIO - TABULEIRO 4 X 4")
    ScreenPrints.get_display_option("WHITE", "3", "DIFÍCIL - TABULEIRO 5 X 5")


def display_level() -> None:
    ScreenPrints.display_header("CRIAR TABULEIRO")

    print("\n\n", "NÍVEIS DE TABULEIRO:".center(170))

    display_option_level()
    ScreenPrints.get_baseboard()
    print(" " * 50, end="* ")


def input_level() -> str:
    display_level()
    user_choice: str = input("INFORME QUAL A OPÇÃO DESEJADA: ")
    ScreenPrints.get_clear_prompt()

    return user_choice


def inicialize() -> str:
    user_choice: str = input_level()

    while not is_valid_level(user_choice):
        user_choice = input_level()

    return convert_option_in_level(user_choice)
