import random
from FilePy.RevealedElement import RevealedElement


class Board:
    """
    Classe que representa um tabuleiro para o jogo das somas escondidas.

    Atributos:
        __level__ (str): O nível de dificuldade do tabuleiro.
        __array_int__ (list[list[int]]): Uma matriz 2D contendo valores inteiros.
        __revealed_int_array__ (list[list[RevealedElement]]): Uma matriz 2D contendo objetos RevealedElement.
        LIMIT_DICT (dict[str, int]): Um dicionário que mapeia os níveis de dificuldade para limites de números aleatórios.
        SIZE_DICT (dict[str, int]): Um dicionário que mapeia os níveis de dificuldade para tamanhos de tabuleiro.
        SIZE (int): O tamanho do tabuleiro.
    """

    def __init__(self, level: str) -> None:
        """
        Inicializa uma instância de Board com o nível de dificuldade especificado.

        Args:
           level (str): O nível de dificuldade (por exemplo, "FÁCIL", "MÉDIO", "DIFÍCIL").
        """
        self.__level__: str = level
        self.__array_int__: list[list[int]] = []
        self.__revealed_int_array__: list[list[RevealedElement]] = []

        self.LIMIT_DICT: dict[str, int] = {"EASY": 30, "AVERAGE": 60, "DIFFICULT": 100}
        self.SIZE_DICT: dict[str, int] = {"EASY": 3, "AVERAGE": 4, "DIFFICULT": 5}
        self.SIZE: int = self.SIZE_DICT[self.__level__]

        self.create_board()
        self.add_tuple_board()

    def create_board(self) -> None:
        """
        Cria o tabuleiro do jogo inicializando e preenchendo matrizes.
        """
        self.create_array()
        self.add_number_board()
        self.add_sum_line()
        self.add_sum_columns()

    def create_array(self) -> None:
        SIZE_ARRAY: int = 6

        for i in range(SIZE_ARRAY):
            line: list[int] = []
            for j in range(SIZE_ARRAY):
                line.append(0)
            self.__array_int__.append(line)

    def add_number_board(self) -> None:
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                self.__array_int__[i][j] = self.get_random_number()

    def get_random_number(self) -> int:
        random_number: int = random.randint(1, self.LIMIT_DICT[self.__level__])

        while not self.is_valid_random_number(random_number):
            random_number: int = random.randint(1, self.LIMIT_DICT[self.__level__])

        return random_number

    def is_valid_random_number(self, random_number: int):
        for i in range(self.SIZE):
            if random_number in self.__array_int__[i]:
                return False

        return True

    def add_sum_line(self) -> None:
        for i in range(self.SIZE):
            sum_line: int = 0
            for j in range(self.SIZE):
                sum_line += self.__array_int__[i][j]
            self.__array_int__[i][self.SIZE] = sum_line

    def add_sum_columns(self) -> None:
        for i in range(self.SIZE):
            sum_column: int = 0
            for j in range(self.SIZE):
                sum_column += self.__array_int__[j][i]
            self.__array_int__[self.SIZE][i] = sum_column

    def add_tuple_board(self) -> None:
        SIZE_ARRAY: int = 6

        for i in range(SIZE_ARRAY):
            line: list[RevealedElement] = []
            for j in range(SIZE_ARRAY):
                line.append(RevealedElement(0))
            self.__revealed_int_array__.append(line)

    def add_relevant_elements(self, list_to_reveal: list[RevealedElement]) -> None:
        for relieved_element in list_to_reveal:
            for i in range(self.SIZE):
                for j in range(self.SIZE):
                    if relieved_element.get_number() == self.__array_int__[i][j]:
                        self.__revealed_int_array__[i][j] = relieved_element

        self.add_relevant_sum()

    def add_relevant_sum(self) -> None:
        for i in range(self.SIZE):
            if self.is_coordinate_complete((f"L{i}", 0)):
                self.__revealed_int_array__[i][self.SIZE] = RevealedElement(self.__array_int__[i][self.SIZE],
                                                                            "\033[1;34m")
        for i in range(self.SIZE):
            if self.is_coordinate_complete((f"C{i}", 0)):
                self.__revealed_int_array__[self.SIZE][i] = RevealedElement(self.__array_int__[self.SIZE][i],
                                                                            "\033[1;34m")

    def count_revealed_houses(self, coordinate: tuple[str, int]) -> int:
        number_of_point: int = 0

        for i in range(self.SIZE):
            if coordinate[0][0] == "L" and not self.is_revealed_house(int(coordinate[0][1]), i):
                number_of_point += 1
            elif coordinate[0][0] == "C" and not self.is_revealed_house(i, int(coordinate[0][1])):
                number_of_point += 1

        return number_of_point

    def is_revealed_house(self, line: int, columns: int) -> bool:
        return self.__array_int__[line][columns] == self.__revealed_int_array__[line][columns].get_number()

    def is_board_complete(self) -> bool:
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if not self.is_revealed_house(i, j):
                    return False

        return True

    def is_coordinate_complete(self, coordinate: tuple[str, int]) -> bool:
        INDEX_COORD: int = int(coordinate[0][1])

        for i in range(self.SIZE):
            if coordinate[0][0] == "L" and not self.is_revealed_house(INDEX_COORD, i):
                return False
            elif coordinate[0][0] == "C" and not self.is_revealed_house(i, INDEX_COORD):
                return False

        return True

    def get_array_int(self) -> list[list[int]]:
        return self.__array_int__

    def get_revealed_int_array(self) -> list[list[RevealedElement]]:
        return self.__revealed_int_array__

    def get_reveal_max(self, coordinate: tuple[str, int], color: str) -> list[RevealedElement]:
        number_max: int = 0
        INDEX_COORD: int = int(coordinate[0][1])

        for i in range(self.SIZE):
            if coordinate[0][0] == "L" and not self.is_revealed_house(INDEX_COORD, i):
                if number_max < self.__array_int__[INDEX_COORD][i]:
                    number_max = self.__array_int__[INDEX_COORD][i]
            elif coordinate[0][0] == "C" and not self.is_revealed_house(i, INDEX_COORD):
                if number_max < self.__array_int__[i][INDEX_COORD]:
                    number_max = self.__array_int__[i][INDEX_COORD]

        return list([RevealedElement(number_max, color)])

    def get_reveal_min(self, coordinate: tuple[str, int], color: str) -> list[RevealedElement]:
        INDEX_COORD: int = int(coordinate[0][1])
        number_min: int = self.LIMIT_DICT[self.__level__] + 1

        for i in range(self.SIZE):
            if coordinate[0][0] == "L" and not self.is_revealed_house(INDEX_COORD, i):
                if number_min > self.__array_int__[INDEX_COORD][i]:
                    number_min = self.__array_int__[INDEX_COORD][i]
            elif coordinate[0][0] == "C" and not self.is_revealed_house(i, INDEX_COORD):
                if number_min > self.__array_int__[i][INDEX_COORD]:
                    number_min = self.__array_int__[i][INDEX_COORD]

        return list([RevealedElement(number_min, color)])

    def get_reveal_all(self, coordinate: tuple[str, int], color: str) -> list[RevealedElement]:
        list_elements: list[RevealedElement] = []
        INDEX_COORD: int = int(coordinate[0][1])

        for i in range(self.SIZE):
            if coordinate[0][0] == "L" and not self.is_revealed_house(INDEX_COORD, i):
                list_elements.append(RevealedElement(self.__array_int__[INDEX_COORD][i], color))
            elif coordinate[0][0] == "C" and not self.is_revealed_house(i, INDEX_COORD):
                list_elements.append(RevealedElement(self.__array_int__[i][INDEX_COORD], color))

        return list_elements

    def get_sum_of_coordinate(self, coordinate: tuple[str, int]) -> int:
        if coordinate[0][0] == "L":
            return self.__array_int__[int(coordinate[0][1])][self.SIZE]

        return self.__array_int__[self.SIZE][int(coordinate[0][1])]

    def __repr__(self) -> str:
        return str(self.__dict__)
