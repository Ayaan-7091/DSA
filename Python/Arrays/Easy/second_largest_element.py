# Retrieving the second largest element 
def retrieve(array):
    n = len(array)
    large = float('-inf')

    for i in range(n):
        large = max(large,array[i])
    
    second_large = i= float('-inf')
    for i in range(n):
        if array[i] > second_large and array[i] != large:
            second_large = array[i]
    return second_large
                    
                
array = [9,7,6,8]
second_highest = retrieve(array)
print(second_highest)