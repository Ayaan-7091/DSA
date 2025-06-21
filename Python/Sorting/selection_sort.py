def selection_sort(array):
    n = len(array)
    for i in range(n):
            for j in range(i+1,n):
                if array[j] < array[i]:
                  array[i], array[j] = array[j], array[i]           
    return array

array = [7,5,8,9,2,3,4,6]
sorted_array = selection_sort(array)
print(sorted_array)