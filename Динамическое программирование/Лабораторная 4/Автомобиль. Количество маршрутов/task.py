from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    # TODO решить задачу с помощью динамического программирования
    # Создаем таблицу dp размером n x m и заполняем ее нулями
    dp = [[0 for _ in range(m)] for _ in range(n)]

    # Инициализируем начальную точку
    dp[0][0] = 1

    # Заполняем таблицу
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue  # Начальная точка уже инициализирована
            paths_from_top = dp[i - 1][j] if i > 0 else 0
            paths_from_left = dp[i][j - 1] if j > 0 else 0
            paths_from_diagonal = dp[i - 1][j - 1] if i > 0 and j > 0 else 0
            dp[i][j] = paths_from_top + paths_from_left + paths_from_diagonal

    return dp


if __name__ == '__main__':
    n, m = 4, 2
    paths = car_paths(n, m)
    print(paths[-1][-1])  # 7

