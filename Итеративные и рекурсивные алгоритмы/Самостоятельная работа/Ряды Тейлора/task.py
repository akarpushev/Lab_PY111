# from typing import Union
# from itertools import count
# from math import factorial
#
#
# DELTA = 0.000001
#
#
# def sinx(x: Union[int, float]) -> float:
#     """
#     Вычисление sin(x) с помощью разложения в ряд Тейлора
#
#     :param x: x значение в радианах
#     :return: значение sin(x)
#     """
#     # TODO вычислить sin(x) с помощью разложения сумму бесконечного ряда
#

from typing import Union
from itertools import count
from math import factorial

DELTA = 0.000001


def sinx(x: Union[int, float]) -> float:
    """
    Вычисление sin(x) с помощью разложения в ряд Тейлора

    :param x: x значение в радианах
    :return: значение sin(x)
    """
    # Начальное значение синуса
    sin_x = 0.0

    # Итеративно вычисляем члены ряда Тейлора
    for n in count(0):
        # Вычисляем текущий член ряда
        term = ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)

        # Добавляем текущий член к сумме
        sin_x += term

        # Проверяем, нужно ли остановиться
        if abs(term) < DELTA:
            break

    return sin_x


# Пример использования
if __name__ == "__main__":
    import math

    x = math.radians(30)  # Пример: 30 градусов в радианах
    print(f"sin({x}) = {sinx(x)}")
    print(f"math.sin({x}) = {math.sin(x)}")  # Для сравнения с результатом библиотеки math
