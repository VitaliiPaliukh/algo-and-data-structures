import csv


def read_data(input_file_direction, output_file_direction):
    edges = []
    vertices = set()
    with open(input_file_direction, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 3:
                k1, k2, distance = row[0], row[1], int(row[2])
                edges.append((k1, k2, distance))
                vertices.add(k1)
                vertices.add(k2)
    dist_to = prim_algorithm(edges, vertices)
    write_output(output_file_direction, dist_to)
    return edges, vertices


def write_output(output_file_direction, dist_to):
    with open(output_file_direction, "w") as file_write:
        file_write.write(str(dist_to))


def prim_algorithm(edges, vertices):
    weights = {vertex: float('inf') for vertex in vertices}
    start_vertex = min(vertices)
    weights[start_vertex] = 0
    queue = [start_vertex]
    visited = {start_vertex}

    while queue:
        min_vertex = min(queue, key=weights.get)
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


read_data("../resource/input_undirected.csv", "../resource/output_undirected_route.txt")
