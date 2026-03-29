
def insertion_sort(lst):
    result = []
    for item in lst:
        # Strict numeric enforcement
        if not isinstance(item, (int, float)):
            raise TypeError(f"insertion_sort only supports numbers, found {type(item)}")
        inserted = False
        index = 0
        while not inserted and index < len(result):
            if item < result[index]:
                result.insert(index, item)
                inserted = True
            index += 1
        if not inserted:
            result.append(item)
    return result