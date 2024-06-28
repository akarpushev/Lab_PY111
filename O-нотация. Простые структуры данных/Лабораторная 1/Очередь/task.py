"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        TODO Описать где начало и конец очереди
        Начало очереди - начало списка (левая сторона).
        Конец очереди - конец списка (правая сторона).
        """
        # TODO инициализировать список
        self.queue = []

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        # TODO реализовать метод enqueue
        self.queue.append(elem)
        # Сложность: O(1) амортизированное время

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        # TODO реализовать метод dequeue
        if not self.queue:
            raise IndexError("Извлечение из пустой очереди невозможно")

        return self.queue.pop(0)
        # Сложность: O(n) из-за смещения всех остальных элементов

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        # TODO реализовать метод peek
        if not isinstance(ind, int):
            raise TypeError(f"Индекс должен быть целочисленного типа, а не {type(ind).__name__}")

        if not 0 <= ind < len(self.queue):
            raise IndexError("Индекс вне границ очереди")

        return self.queue[ind]
        # Сложность: O(1), так как доступ по индексу в списке имеет постоянное время

    def clear(self) -> None:
        """ Очистка очереди. """
        # TODO реализовать метод clear
        self.queue.clear()
        # Сложность: O(n), так как требуется удаление всех элементов из списка

    def __len__(self):
        """ Количество элементов в очереди. """
        # TODO реализовать метод __len__
        return len(self.queue)
        # Сложность: O(1), так как доступ к длине списка имеет постоянное время

#
# # Пример использования:
# if __name__ == '__main__':
#     q = Queue()
#     q.enqueue(1)
#     q.enqueue(2)
#     q.enqueue(3)
#     print(q.dequeue())  # 1
#     print(q.peek())  # 2
#     print(len(q))  # 2
#     q.clear()
#     print(len(q))  # 0
