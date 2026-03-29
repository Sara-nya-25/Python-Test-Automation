
def bubble_sort(lst):
    n = len(lst)
    # Copy the list to avoid modifying the original (keeping it consistent with your others)
    result = list(lst)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                # Swap if the element found is greater than the next element
                result[j], result[j + 1] = result[j + 1], result[j]
    return result