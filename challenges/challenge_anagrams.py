from utils.merge_sort import merge_sort


def is_anagram(first_string, second_string):
    first_str_sorted = ''.join(merge_sort(list(first_string.lower())))
    second_str_sorted = ''.join(merge_sort(list(second_string.lower())))

    if first_string == '' and second_string == '':
        compair = False
    else:
        compair = first_str_sorted == second_str_sorted

    return (
        first_str_sorted,
        second_str_sorted,
        compair,
    )
