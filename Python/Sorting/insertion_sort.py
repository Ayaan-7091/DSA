def insertion_sort(array):
    n = len(array)
    for i in range(1,n):
        temp = array[i]
        j = i - 1
        while array[j] > temp and j>=0:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = temp

    return array

array = [10,2,8,7,1,3,5,6,4,9]
sorted_array = insertion_sort(array)
print(sorted_array)