from FilePy import ScreenPrints


def check_board_number(user_choice: int) -> None:
    set_option: set[int] = {1, 2}

    if user_choice not in set_option:
        raise RuntimeError("O tabuleiro informado não está disponível")


def is_valid_board_number(use_choice: int) -> bool:
    try:
        check_board_number(use_choice)
        return True
    except RuntimeError as error:
        ScreenPrints.get_report_error(error.__str__())
        return False


def display_option_board_number() -> None:
    ScreenPrints.get_display_option("WHITE", "1", "1 Tabuleiro")
    ScreenPrints.get_display_option("BLUE", "2", "2 Tabuleiros")


def display_board_number() -> None:
    ScreenPrints.display_header("CRIAR TABULEIRO")

    print("\n\n", "TABULEIROS DISPONÍVEIS:".center(170))

    display_option_board_number()
    ScreenPrints.get_baseboard()
    print(" " * 50, end="* ")


def input_board_number() -> int:
    try:
        display_board_number()
        user_choice: int = int(input("INFORME QUAL A OPÇÃO DESEJADA: "))
        ScreenPrints.get_clear_prompt()
        return user_choice
    except ValueError:
        return -1


def inicialize() -> int:
    user_choice: int = input_board_number()

    while not is_valid_board_number(user_choice):
        user_choice = input_board_number()

    return user_choice
