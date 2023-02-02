def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False
    if low_index >= high_index:
        return True
    if word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    else:
        return False


if __name__ == "__main__":
    teste = is_palindrome_recursive(word="coxinha", low_index=-1, high_index=0)
    print(teste)
