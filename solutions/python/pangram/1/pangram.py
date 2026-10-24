def is_pangram(sentence):
    all_chars_in_sentence = set(sentence.lower())    # set all letters to one case
    unique_letter_count = 0
    for char in all_chars_in_sentence:
        if 'a' <= char <= 'z':
            unique_letter_count += 1
    return unique_letter_count == 26