# Problem Statement: Given an integer N and an array of size N-1,
# containing N-1 numbers between 1 to N. Find the number(between 1 to N), that is not present in the given array.

# Initial Approach
def test(n,arr):
    temp = [0]*n
    for i in range(n):
        temp[i] = i+1
        
    for i in range(n):
        if temp[i] != arr[i]:
                return temp[i]

arr = [1,2,4,5]
n = 5
print(test(n,arr))