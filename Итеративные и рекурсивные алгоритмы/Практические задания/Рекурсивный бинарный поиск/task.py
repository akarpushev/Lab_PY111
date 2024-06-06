from typing import Sequence


def binary_search(
        value: int, seq: Sequence[int],
        left_border: int = 0, right_border: int = None
) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск
    :param left_border: Левая граница массива, нужна для рекурсивного алгоритма
    :param right_border: Правая граница массива, нужна для рекурсивного алгоритма

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    if right_border is None:
        right_border = len(seq) -1

    if left_border > right_border:
        raise ValueError("Элемента нет")

    middle_index = left_border + (right_border - left_border) // 2
    middle_value = seq[middle_index]

    if value == middle_value:
        #return middle_index
        while True:
            if not 0 <= middle_index - 1 <= len(seq) or seq[middle_index - 1] != value:
                break
            else:
                middle_index -= 1
        return middle_index

    elif middle_value < value:
        left_border = middle_index + 1
    else:
        right_border = middle_index -1
    return binary_search(value, seq, left_border, right_border)



    # TODO реализовать алгоритм бинарного поиска

print(binary_search(4, [0, 1, 2, 3, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

