from FilePy import ScreenPrints


def check_option(number_of_round: int, level: str) -> None:
    rounds_by_level_dict: dict[str, int] = {"EASY": 9, "AVERAGE": 16, "DIFFICULT": 25}

    if number_of_round < 1:
        raise RuntimeError("O número de rodadas informado é invalido")
    elif number_of_round > rounds_by_level_dict[level]:
        raise RuntimeError(f"O número de rodadas informado é maior que o limite do nível de "
                           f"{rounds_by_level_dict[level]}")
    elif number_of_round % 2 == 0:
        raise RuntimeError("O número de rodadas informado não pode ser par")


def is_valid_option_two(number_of_round: int, level: str) -> bool:
    try:
        check_option(number_of_round, level)
        return True
    except RuntimeError as error:
        ScreenPrints.get_report_error(error.__str__())
        return False


def check_number_of_rounds(user_choice: int) -> None:
    set_options: set[int] = {1, 2}

    if user_choice not in set_options:
        raise RuntimeError("A maneira de finalizar o jogo informada não existe")


def is_valid_number_of_rounds(user_choice: int) -> bool:
    try:
        check_number_of_rounds(user_choice)
        return True
    except RuntimeError as error:
        ScreenPrints.get_report_error(error.__str__())
        return False


def input_option_two() -> int:
    try:
        print(" " * 49, end="* ")
        user_choice: int = int(input("INFORME O NÚMERO DE RODADAS DESEJADA: "))
        ScreenPrints.get_clear_prompt()
        return user_choice
    except ValueError:
        ScreenPrints.get_clear_prompt()
        return -1


def define_number_of_rounds(user_choice: int) -> int:
    OPTION_TWO: int = 2
    NUMBER_OF_COMPLETED_GAMES: int = 9

    if user_choice == OPTION_TWO:
        return input_option_two()

    return NUMBER_OF_COMPLETED_GAMES


def display_option_rounds() -> None:
    ScreenPrints.get_display_option("WHITE", "1", "COMPLETA TABULEIRO")
    ScreenPrints.get_display_option("BLUE", "2", "DEFINIR NÚMERO DE RODADAS")


def display_rounds() -> None:
    ScreenPrints.display_header("CRIAR TABULEIRO")

    print("\n" * 2, "NÚMERO DE RODADAS:".center(170))

    display_option_rounds()
    ScreenPrints.get_baseboard()
    print(" " * 50, end="* ")


def input_number_of_rounds() -> int:
    try:
        display_rounds()
        user_choice: int = int(input("INFORME QUAL A OPÇÃO DESEJADA: "))
        ScreenPrints.get_clear_prompt()
        return user_choice
    except ValueError:
        ScreenPrints.get_clear_prompt()
        return -1


def inicialize(level: str) -> int:
    user_choice: int = input_number_of_rounds()
    number_of_round: int = define_number_of_rounds(user_choice)

    while not (is_valid_number_of_rounds(user_choice) and is_valid_option_two(number_of_round, level)):
        user_choice = input_number_of_rounds()
        number_of_round = define_number_of_rounds(user_choice)

    return number_of_round
