def find(search_list, value):
    sorted_list = sorted(search_list)
    
    start, end = 0, len(sorted_list) - 1
    
    while start <= end:
        mid = start + (end - start) // 2

        if sorted_list[mid] == value:
            return mid
        elif sorted_list[mid] > value:
            end = mid - 1
        else:
            start = mid + 1

    raise ValueError("value not in array")