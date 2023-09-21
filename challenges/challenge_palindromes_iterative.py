def is_palindrome_iterative(word):
    if word == '':
        return False

    min_index = 0
    max_index = len(word) - 1

    while min_index < max_index:
        if word[min_index] != word[max_index]:
            return False

        min_index += 1
        max_index -= 1

    return True
