#Retrieve the largest element form the array

#Brute Force Approach
def retrieve(array):
    n = len(array)

    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    
    return array[n-1]

array = [3,2,4,6,9]
print(retrieve(array))

# Recursive Approarch