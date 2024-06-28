from typing import Union, Tuple
import networkx as nx
#import matplotlib.pyplot as plt


def build_stairway_graph(stairway: Tuple[int]) -> nx.DiGraph:
    """
    Построить взвешенный направленный граф для лестницы с заданными стоимостями ступенек.

    :param stairway: Кортеж со стоимостями ступенек
    :return: Взвешенный направленный граф
    """
    G = nx.DiGraph()

    # Добавляем узлы и ребра в граф
    for i in range(len(stairway)):
        if i + 1 < len(stairway):  # Переход на следующую ступень
            G.add_edge(i, i + 1, weight=stairway[i + 1])
        if i + 2 < len(stairway):  # Перепрыгивание через одну ступень
            G.add_edge(i, i + 2, weight=stairway[i + 2])

    return G


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитать минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    # TODO c помощью функции из модуля networkx найти стоимость кратчайшего пути до последней лестницы
    start = 0
    end = max(graph.nodes)

    # Используем алгоритм Дейкстры для нахождения минимальной стоимости пути до последней вершины
    return nx.shortest_path_length(graph, source=start, target=end, weight='weight')


if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)

    # TODO записать взвешенный граф, а лучше написать функцию, которая формирует граф по стоимости ступеней
    # Создание графа по стоимости ступеней
    stairway_graph = build_stairway_graph(stairway)

    # Рассчет минимальной стоимости подъема
    print(stairway_path(stairway_graph))  # Ожидаемое значение: 72

    # graph = build_stairway_graph(stairway)
    # nx.draw(graph)
    # plt.show()





