import csv
from typing import List, Tuple, Set


def read_data(input_file_direction: str, output_file_direction: str) -> Tuple[List[Tuple[str, str, int]], Set[str]]:
    """
    :param input_file_direction: the direction of the input file
    :param output_file_direction: the direction of the output file
    :return: a list of all vertices and a list of edges in the format (k1, k2, weight)
     """
    edges: List[Tuple[str, str, int]] = []
    vertices: Set[str] = set()
    with open(input_file_direction, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 3:
                cur_vertex, next_vertex, distance = row[0], row[1], int(row[2])
                edges.append((cur_vertex, next_vertex, distance))
                vertices.add(cur_vertex)
                vertices.add(next_vertex)
    dist_to = prim_algorithm(edges, vertices)
    write_output(output_file_direction, dist_to)
    return edges, vertices


def write_output(output_file_direction, dist_to):
    with open(output_file_direction, "w") as file_write:
        file_write.write(str(dist_to))


def prim_algorithm(edges: List[Tuple[str, str, int]], vertices: Set[str]) -> int:
    """
    :param edges:
    :param vertices:
    :return: -1 if set(vertices) != visited: else return the sum of the weights
    """
    weights = {vertex: float('inf') for vertex in vertices}
    start_vertex = min(vertices)
    weights[start_vertex] = 0
    queue = [start_vertex]
    visited = {start_vertex}
#todo: use priority queue
    while queue:
        min_vertex = min(queue, key=weights.get)  # rename min_vertex to min_edge
        queue.remove(min_vertex)
        for edge in edges:
            if edge[0] == min_vertex and edge[1] not in visited and weights[edge[1]] > edge[2]:
                weights[edge[1]] = edge[2]
                queue.append(edge[1])
                visited.add(edge[1])
            elif edge[1] == min_vertex and edge[0] not in visited and weights[edge[0]] > edge[2]:
                weights[edge[0]] = edge[2]
                queue.append(edge[0])
                visited.add(edge[0])

    if set(vertices) != visited:
        return -1

    return sum(weights.values())
