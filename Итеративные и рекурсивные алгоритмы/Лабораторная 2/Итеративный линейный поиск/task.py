"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    # TODO реализовать итеративный линейный поиск
    if not arr:
        raise ValueError("Массив не может быть пустым")

    # Начинаем с предположения, что первый элемент - минимальный
    min_index = 0
    min_value = arr[0]

    # Проходим по массиву, начиная со второго элемента
    for i in range(1, len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
            min_index = i

    return min_index


# Пример использования:
# if __name__ == '__main__':
#     example_array = [5, 3, 1, 7, 4, 1, 2]
#     print("Индекс минимума:",
#           min_search(example_array))
# Ожидаемый результат: 2 (минимум это 1, первый раз встречается на индексе 2)