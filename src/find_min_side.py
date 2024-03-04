def min_long(n: int, w: int, h: int) -> int:
    area = w * h
    temp_w, temp_h = w, h
    while (temp_w * temp_h) / area < n:
        if temp_h + h >= temp_w + w:
            temp_w += w
        else:
            temp_h += h
    return max(temp_w, temp_h)
