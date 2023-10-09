from Inputs import MainMenu


if __name__ == '__main__':
    user_choice: int = MainMenu.get_main_manu_entry()

    while not MainMenu.is_exit_option(user_choice):
        MainMenu.open_option(user_choice)
        user_choice: int = MainMenu.get_main_manu_entry()

