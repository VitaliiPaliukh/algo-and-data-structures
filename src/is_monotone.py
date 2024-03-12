def is_monotone(arr):
    def is_increasing():
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

    def is_decreasing():
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                return False
        return True

    return is_increasing() or is_decreasing()
