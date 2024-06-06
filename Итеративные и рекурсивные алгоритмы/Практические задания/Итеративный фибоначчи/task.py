def fib_iterative(n: int) -> int:
    """
    Вычислить n-е число последовательности Фибоначчи, используя итеративный алгоритм.

    :param n: Номер числа последовательности Фибоначии. Нумерация чисел с 0
    :return: n-е число последовательности Фибоначчи
    """
    a, b = 0, 1

    if n == 0:
        return a

    if n == 1:
        return b

    for i in range(2, n + 1):
        a, b = b, a + b
    #return a, b
    return b
    # TODO написать итеративный алгоритм чисел Фибоначчи


if __name__ == '__main__':
    print(fib_iterative(9))
    print([fib_iterative(i) for i in range(10)])