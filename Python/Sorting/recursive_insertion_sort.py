def insertion_sort(array,i=1):
    n = len(array)

    if i >= n:
        return array
    temp = array[i]
    j = i-1
    while array[j] > temp and j>=0:
        array[j+1] = array[j]
        j = j - 1
    array[j+1] = temp
    
    return insertion_sort(array,i+1)

array = [9,7,8,6,4,2,1,5,3]
sorted_array = insertion_sort(array)
print(sorted_array)
            
