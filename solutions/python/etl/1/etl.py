def transform(legacy_data):
    data = {}
    for point_value, letter_list in legacy_data.items():
        for letter in letter_list:
            data[chr(ord(letter) + 32)] = point_value

    return dict(sorted(data.items()))
