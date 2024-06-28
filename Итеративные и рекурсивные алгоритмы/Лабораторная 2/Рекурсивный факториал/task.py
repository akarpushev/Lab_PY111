#import functools

#@functools.lru_cache()
def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    # TODO реализовать рекурсивный алгоритм нахождения факториала
    if not isinstance(n, int):
        raise TypeError("Факториал определен только для неотрицательных целых чисел")

    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных целых чисел")

    # Базовый случай: 0! = 1
    if n == 0:
        return 1

    # Рекурсивный случай: n! = n * (n-1)!
    return n * factorial_recursive(n - 1)

#Примеры использования:
if __name__ == '__main__':
    print(factorial_recursive(5))  # 120
    print(factorial_recursive(0))  # 1
    print(factorial_recursive(10)) # 3628800