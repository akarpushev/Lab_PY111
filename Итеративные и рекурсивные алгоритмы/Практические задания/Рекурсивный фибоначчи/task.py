import functools

cashe = {'count': 0}

count = 0

@functools.lru_cache()
def fib_recursive(n: int) -> int:
    """
    Вычислить n-е число последовательности Фибоначчи, используя рекурсивный алгоритм.

    :param n: Номер числа последовательности Фибоначии. Нумерация чисел с 0
    :return: n-е число последовательности Фибоначчи
    """
    global count
    a, b = 0, 1

    if n == 0:
        #count += 1
        cashe['count'] +=1
        return a

    if n == 1:
        #count += 1
        cashe['count'] += 1
        return b

    #count += 1
    cashe['count'] += 1

    return fib_recursive(n-1) + fib_recursive(n-2)

print(fib_recursive(8))

#print(count)
print(cashe)

    # TODO реализовать рекурсивный алгоритм
