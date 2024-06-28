def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    # TODO реализовать итеративный алгоритм нахождения факториала
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел")

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

# Примеры использования:
# if __name__ == '__main__':
#     print(factorial_iterative(5))  # 120
#     print(factorial_iterative(0))  # 1
#     print(factorial_iterative(10)) # 3628800
