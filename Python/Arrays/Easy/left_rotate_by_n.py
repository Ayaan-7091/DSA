def left_rotate(array,k):
    n = len(array)
    temp = [0]*k

    for i in range(k):
        temp[i] = array[i]    
    i = 0
    for j in range(k,n):
        if i<n-1:
            print(j)
            array[i] = array[j]
            i += 1
    i = 0   
    for s in range(n-k,n):
        if i < n - 1:
            array[s] = temp[i]
            i += 1

    return array

array = [1,2,3,4,5,6,7,8]
result = left_rotate(array,4)
print(result)

#shorted approach :
def left_rotate_sh(array, k):
    n = len(array)
    k = k % n  # Optional: To handle k > n
    temp = array[:k]  # Save first k elements

    # Shift the remaining elements left
    for i in range(n - k):
        array[i] = array[i + k]

    # Place the saved k elements at the end
    for i in range(k):
        array[n - k + i] = temp[i]

    return array

array = [1, 2, 3, 4, 5, 6, 7, 8]
result = left_rotate_sh(array, 4)
print(result)  # [5, 6, 7, 8, 1, 2, 3, 4]
