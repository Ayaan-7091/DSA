def selection_sort(array,i):
    n = len(array)
    if i<n:
        for j in range(i+1,n):
            if array[j]<array[i]:
                array[i],array[j] = array[j],array[i]
        selection_sort(array,i+1)
    else:
        print(array)
array = [5,4,2,1,3]
selection_sort(array,0)
    