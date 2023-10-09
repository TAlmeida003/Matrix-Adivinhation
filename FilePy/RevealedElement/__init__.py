class RevealedElement:

    def __init__(self, number: int, color: str = "\033[1;97m") -> None:
        self.__number__: int = number
        self.__color__: str = color

    def set_color(self, color: str) -> None:
        self.__color__ = color

    def get_str(self) -> str:
        txt: str = str(self.__number__) if self.__number__ != 0 else "    "
        return self.__color__ + txt + "\033[1;97m"

    def get_number(self) -> int:
        return self.__number__

    def __repr__(self) -> str:
        return str(self.__number__)

    def in_list(self, list_elements: list) -> bool:
        for i in list_elements:
            if i.get_number() == self.__number__:
                return True
        return False

    def index_list(self, list_elements: list) -> int:
        for i in range(len(list_elements)):
            if list_elements[i].get_number() == self.__number__:
                return i
        return -1
