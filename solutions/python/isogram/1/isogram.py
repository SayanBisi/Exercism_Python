def is_isogram(phrase):
    one_case = phrase.lower()
    letter_appears_once = True
    for char in one_case:
        if 'a' <= char <= 'z':
            substring = one_case[one_case.index(char) + 1:]
            if char in substring:
                letter_appears_once = False
                break

    return letter_appears_once