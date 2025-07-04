# check if the given array is sorted

def check(array):
    n = len(array)
    isSorted = True
    for i in range(n):
        for j in range(i+1,n):
            if array[i] > array[j]:
                isSorted = False
    if isSorted:
        return "Sorted"
    else:
        return "Not Sorted"
           

array = [1,2,3,4,5,6]
array_2 = [7,9,6,8,5]

print(check(array))
print(check(array_2))

def check_optimal(array):
    n = len(array)
    check = True
    for i in range(1,n):
        if array[i-1] > array[i]:
            check = False
    
    if check:
        return "Sorted"
    else:
        return "Not Sorted"

print(check_optimal(array))
print(check_optimal(array_2))
