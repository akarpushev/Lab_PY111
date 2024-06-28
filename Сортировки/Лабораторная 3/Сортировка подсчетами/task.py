from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    # TODO реализовать алгоритм сортировки подсчетами
    if not container:
        return []

    max_value = max(container)

    # Шаг 1: Инициализируем массив count с размерами от 0 до max_value.
    count = [0] * (max_value + 1)

    # Шаг 2: Подсчитываем количество каждого элемента в исходном массиве.
    for number in container:
        count[number] += 1

    # Шаг 3: Восстанавливаем отсортированный массив.
    sorted_container = []
    for number, freq in enumerate(count):
        sorted_container.extend([number] * freq)

    return sorted_container


# Примеры использования
if __name__ == '__main__':
    example = [4, 2, 2, 8, 3, 3, 1, 0]
    print(sort(example))  # Ожидаемый результат: [0, 1, 2, 2, 3, 3, 4, 8]
