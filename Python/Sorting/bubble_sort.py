def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    
    return array

array = [10,2,8,7,1,3,5,6,4,9]
sorted_array = bubble_sort(array)
print(sorted_array)

def optimized_bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                swapped = True
        if not swapped:
            break
    return array

optimal_sorted_array = optimized_bubble_sort(array)
print(optimal_sorted_array)