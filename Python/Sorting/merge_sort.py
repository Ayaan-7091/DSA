def merge_sort(array):
    if len(array) <= 1:
        return array  # Base case: already sorted

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    return merge(sorted_left, sorted_right)


def merge(left, right):
    merged = []
    i = 0
    j = 0

    # While both have elements
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append the rest from either side
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


array = [1,8,5,6,2]
sorted_array = merge_sort(array)
print(sorted_array)