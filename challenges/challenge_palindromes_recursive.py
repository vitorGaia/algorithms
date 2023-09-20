def is_palindrome_recursive(word, min_index, max_index):
    if word == '':
        return False

    if min_index >= max_index:
        return True

    if word[min_index] != word[max_index]:
        return False

    return is_palindrome_recursive(word, min_index + 1, max_index - 1)
