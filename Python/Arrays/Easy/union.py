#calculating the union of two arrays

#first attempt
def union(arr1,arr2):
    for i in range(len(arr2)):
        arr1.append(arr2[i])
    arr1 = list(set(arr1))
    return arr1

#better approach
def union_bt(arr1, arr2):
    return list(set(arr1 + arr2))




arr1 = [1,2,3,4,5]
arr2 = [4,5,6,7,8]
result = union(arr1,arr2)
print(result)