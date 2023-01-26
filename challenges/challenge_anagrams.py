def is_anagram(first_string: str, second_string: str):
    word_1 = list(first_string.lower())
    string_1 = "".join(quicksort(word_1))
    word_2 = list(second_string.lower())
    string_2 = "".join(quicksort(word_2))

    if string_1 == "" and string_2 == "":
        return (string_1, string_2, False)
    if string_1 == string_2:
        return (string_1, string_2, True)
    else:
        return (string_1, string_2, False)


def quicksort(lst):
    if not lst:
        return []
    return (quicksort([x for x in lst[1:] if x < lst[0]])
            + [lst[0]] +
            quicksort([x for x in lst[1:] if x >= lst[0]]))
