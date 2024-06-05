"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        TODO Описать где начало и конец очереди
        """
        self.queue = list()
        self.start = self.queue[::-1]
        self.end = self.queue[0]

        # TODO инициализировать список

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        self.queue.insert(self.end, elem)
        # TODO реализовать метод enqueue

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        for elem in self.queue:
            if elem:
                return elem.pop(self.start)

        raise IndexError("Извлечение из пустой очереди не возможно")
        # TODO реализовать метод dequeue

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            raise TypeError(f"Индекс должен быть целочисленного типа, а не {type(ind).__name__}")

        if not 0 <= ind < len(self.queue):
            raise IndexError("Индекс все границ очереди")

        return self.queue[ind]
        # TODO реализовать метод peek

    def clear(self) -> None:
        """ Очистка очереди. """
        self.queue.clear()
        # TODO реализовать метод clear

    def __len__(self):
        """ Количество элементов в очереди. """
        return len(self.queue)
        # TODO реализовать метод __len__
