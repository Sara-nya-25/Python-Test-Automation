"""
Time Complexity:
The time complexity of this function is O(n^2).
The Outer Loop: Runs n times (once for each element in the input list).
The Inner Loop/Insert: In the worst-case scenario (a reverse-sorted list),
you have to compare the new item with every item already in result.
Additionally, the .insert() method itself is an O(n) operation because it has to shift all subsequent elements in memory.
Total: n iterations times n work per iteration = O(n^2).
"""
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