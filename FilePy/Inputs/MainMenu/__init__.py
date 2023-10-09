from FilePy import ScreenPrints, Game


def open_option(user_choice_option: int) -> None:
    OPTION_ONE: int = 1

    if user_choice_option == OPTION_ONE:
        Game.inicialize()
    else:
        pass


def is_exit_option(user_choice: int) -> bool:
    OPTION_EXIT: int = 3

    if user_choice != OPTION_EXIT:
        return False

    return True


def check_option_main_menu(user_choice: int) -> None:
    set_option: set[int] = {1, 2, 3}

    if user_choice not in set_option:
        raise RuntimeError("OPÇÃO INVALIDA")


def is_a_valid_main_menu_option(user_choice: int) -> bool:

    try:
        check_option_main_menu(user_choice)
        return True
    except RuntimeError as error:
        ScreenPrints.get_report_error(error.__str__())
        return False


def display_options() -> None:
    ScreenPrints.get_display_option("BLUE", "1", "NOVO JOGO")
    ScreenPrints.get_display_option("WHITER", "2", "TUTORIAL DO JOGO")
    ScreenPrints.get_display_option("BLUE", "3", "FECHA JOGO")


def display_main_menu() -> None:
    ScreenPrints.display_header('MENU PRINCIPAL')
    display_options()
    ScreenPrints.get_baseboard()
    print(" " * 50, end="* ")


def input_main_menu_option() -> int:
    try:
        display_main_menu()
        user_choice: int = int(input("INFORME QUAL A OPÇÃO DESEJADA: "))
        ScreenPrints.get_clear_prompt()
        return user_choice
    except ValueError:
        ScreenPrints.get_clear_prompt()
        return -1


def get_main_manu_entry() -> int:

    user_choice: int = input_main_menu_option()

    while not is_a_valid_main_menu_option(user_choice):
        user_choice = input_main_menu_option()

    return user_choice
