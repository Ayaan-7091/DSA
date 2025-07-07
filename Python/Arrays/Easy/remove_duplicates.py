#simpler approach
def test_0(array):
    return list(set(array))

array = [1,2,2,3,4,4,5]
print(test_0(array))


#Brute force approach
def remove_duplicate(array):
    n = len(array)
    st = set()

    for i in range(n):
        st.add(array[i])
    k = len(st)
    j = 0
    for x in st:
        array[j] = x
        j = j + 1
    return k


arr = [1, 1, 2, 2, 2, 3, 3]
k = remove_duplicate(arr)
print("The array after removing duplicate elements is ")
for i in range(k):
    print(arr[i], end=" ")
print("\n")

#Optimal Approach - using two pointers

def remove_duplicate_op(array):
    n = len(array)
    i = 0  # Slow pointer
    for j in range(1, len(array)):  # Fast pointer
        if array[j] != array[i]:
            i += 1
            array[i] = array[j]
    
    return i + 1  # Length of unique elements


array = [1,2,2,3,4,4,4,5]
n  =  remove_duplicate_op(array)
for i in range(n):
    print(array[i],end=" ")