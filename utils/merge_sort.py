def merge_sort(array, start=0, end=None):
    if end is None:
        end = len(array)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(array, start, mid)
        merge_sort(array, mid, end)
        merge(array, start, mid, end)
    return array


def merge(array, start, mid, end):
    left = array[start:mid]
    right = array[mid:end]
    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            array[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            array[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            array[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            array[general_index] = right[right_index]
            right_index = right_index + 1
