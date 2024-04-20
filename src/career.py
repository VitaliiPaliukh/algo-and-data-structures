def find_max_experience(levels, positions):
    max_experience = 0
    current_level_index = levels - 1
    stack = []

    for current_position_index in range(len(positions[current_level_index])):
        stack.insert(0, [current_level_index, current_position_index, positions[current_level_index][current_position_index]])
        while stack:
            current_node = stack.pop(-1)
            current_level = current_node[0]
            current_position = current_node[1]
            current_experience = current_node[2]
            if current_level != 0:
                if current_position == 0:
                    stack.insert(0, [current_level - 1, 0, current_experience + positions[current_level - 1][current_position]])
                elif current_position == len(positions[current_level]) - 1:
                    stack.insert(0, [current_level - 1, current_position - 1,
                                     current_experience + positions[current_level - 1][current_position - 1]])
                else:
                    stack.insert(0, [current_level - 1, current_position, current_experience + positions[current_level - 1][current_position]])
                    stack.insert(0, [current_level - 1, current_position - 1,
                                     current_experience + positions[current_level - 1][current_position - 1]])
            else:
                if current_experience > max_experience:
                    max_experience = current_experience
    return max_experience


def read_input(input_file_direction, output_file_direction):
    file_read = open(input_file_direction, "r")
    try:
        levels = int(file_read.readline())
        matrix = []
        for _ in range(levels):
            row = list(map(int, file_read.readline().split()))
            matrix.append(row)
    except ValueError:
        write_output(output_file_direction, -1)
        file_read.close()
        return
    file_read.close()
    experience = find_max_experience(levels, matrix)
    write_output(output_file_direction, experience)


def write_output(output_file_direction, experience):
    file_write = open(output_file_direction, "w")
    file_write.write(str(experience))
    file_write.close()


read_input("../resource/career_input.txt", "../resource/career_output.txt")
