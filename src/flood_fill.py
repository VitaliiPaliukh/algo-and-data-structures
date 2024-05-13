def read_input(input_file_direction, output_file_direction):
    file_read = open(input_file_direction, "r")
    try:
        size_matrix_row, size_matrix_col = tuple(map(int, file_read.readline().split(',')))
        coordinate = tuple(map(int, file_read.readline().split(',')))
        replacement_color = file_read.readline()[0]
        matrix = []
        for i in range(size_matrix_row):
            matrix_row = list(file_read.readline().split(", "))
            matrix_row[-1] = matrix_row[-1][:1]
            matrix.append(matrix_row)
    except ValueError:
        write_output(output_file_direction, -1)
        file_read.close()
        return
    file_read.close()
    matrix = flood_fill(matrix, coordinate, replacement_color)
    write_output(output_file_direction, matrix)


def write_output(output_file_direction, matrix):
    file_write = open(output_file_direction, "w")
    if matrix == -1:
        file_write.write("-1")
    else:
        for i in matrix:
            file_write.write(str(i)+"\n")
    file_write.close()


def get_color(matrix, coordinate):
    row, col = coordinate
    return matrix[row][col]


def flood_fill(matrix, start_point, replacement_color):
    queue = [start_point]
    target_color = get_color(matrix, start_point)
    if target_color == replacement_color:
        return matrix

    while queue:
        rows, cols = queue.pop(0)
        if matrix[rows][cols] == target_color:
            matrix[rows][cols] = replacement_color
        for delta_rows in range(-1, 2):
            for delta_cols in range(-1, 2):
                neighbor_rows = delta_rows + rows
                neighbor_cols = delta_cols + cols
                if 0 <= neighbor_rows < len(matrix) and 0 <= neighbor_cols < len(matrix[0]) and \
                        matrix[neighbor_rows][neighbor_cols] == target_color:
                    queue.append([neighbor_rows, neighbor_cols])
    return matrix


read_input("../resource/input_same_color.txt", "../resource/output_same_color.txt")