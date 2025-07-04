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

# Recursive Approach
def recursive_retrieve(array,max=array[0],i=0):
    n = len(array)
    if i >= n:
        return max
    if array[i]>max:
        max = array[i]
    return recursive_retrieve(array,max,i+1)  

array = [8,6,7,5,9]
highest_element = recursive_retrieve(array)
print(highest_element)  

