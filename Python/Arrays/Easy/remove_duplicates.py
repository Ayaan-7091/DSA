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

#Better approach