def rotate_left(array):
    n = len(array)
    temp = array[0]

    for i in range(n):
        if i < n-1:
            array[i] = array[i+1]
        else:
            array[n-1] = temp
    return array

array = [1,2,3,4,5,6]
print(rotate_left(array))
        
