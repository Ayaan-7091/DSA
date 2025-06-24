def bubble_sort(array,x=0):
    n = len(array)
    if x >= n:
        return array
    
    for j in range(n-1-x):
        if array[j] > array[j+1]:
            array[j],array[j+1] = array[j+1],array[j]
    return bubble_sort(array,x+1)

array = [9,7,8,6,4,2,1,5,3]
sorted_array = bubble_sort(array)
print(sorted_array)