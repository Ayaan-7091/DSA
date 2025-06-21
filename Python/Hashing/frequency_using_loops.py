def fetch_frequency(n,array):
    visited = [False] * n
    for i in range(n):
        if (visited[i] == True):
            continue
        count = 1
        for j in range(i+1,n):
            if(array[i]==array[j]):
                visited[j] = True
                count += 1
        print(array[i],count)

arr = [10, 5, 10, 15, 10, 5]
n = 6
fetch_frequency(6,arr) 