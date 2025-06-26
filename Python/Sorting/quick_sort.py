def quick_sort(array,low,high):
    if low < high:
        #retrieving the pivot index by partitioning
        pivot_index = partition(array, low, high)

        #recursively applying quick sort to sort subarrays
        quick_sort(array,low,pivot_index-1)
        quick_sort(array,pivot_index+1,high) 

def partition(array,low,high):
    #I am by default taking the last element as the pivot, so I have to take all small elements preceding it 
    pivot = array[high]
    i = low - 1

    for j in range(low,high):
        if array[j] < pivot:
            i += 1
            array[i],array[j] = array[j],array[i]
        
    array[i+1],array[high] = array[high],array[i+1]
    return i+1

array = [9,8,5,1,2,4,6,7,3]
quick_sort(array,0,len(array)-1)
print(array)