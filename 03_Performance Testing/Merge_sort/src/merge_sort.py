"""
Time Complexity:
The time complexity of this function is O(n^2).
The Outer Loop: Runs n times (once for each element in the input list).
The Inner Loop/Insert: In the worst-case scenario (a reverse-sorted list),
you have to compare the new item with every item already in result.
Additionally, the .insert() method itself is an O(n) operation
because it has to shift all subsequent elements in memory to make room.
Total: n iterations times n work per iteration = O(n^2).
"""

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
