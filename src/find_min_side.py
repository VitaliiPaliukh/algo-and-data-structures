def find_min_side(number_notes: int, width: int, height: int) -> int:
    area = width * height
    temp_width, temp_height = width, height
    while (temp_width * temp_height) / area < number_notes:
        if temp_height + height >= temp_width + width:
            temp_width += width
        else:
            temp_height += height
    return max(temp_width, temp_height)

