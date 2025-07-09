# Move all the zeroes to the right side while preserving the order

#initial instinct approach
def move(arr):
    n = len(arr)
    temp = []

    for i in range(n):
        if arr[i] == 0:
            temp.append(arr[i])
            
            if arr[i+1] == 0:
                arr[i] = arr[i+2]
            else:
                arr[i] = arr[i+1]

    arr = list(set(arr))
    
    for i in range(len(temp)):
        arr.append(temp[i])

    return arr

arr = [1,0,0,2,3,0,0,4,0,5]
result = move(arr)
print(result)

# Better Approach
def move_bt(arr):
    n = len(arr)
    j = 0

    for i in range(n):
        if arr[i] != 0:
            arr[i],arr[j] = arr[j],arr[i]
            j += 1
    
    return arr

arr = [1, 0, 0, 2, 3, 0, 0, 4, 0, 5]
result = move_bt(arr)
print(result)
