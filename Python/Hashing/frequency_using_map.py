def fetch_frequency(n,array):
    mp = {}

    for i in range(n):
        if array[i] in mp:
            mp[array[i]] += 1
        else :
            mp[array[i]] = 1
    
    return mp

arr = [10, 5, 10, 15, 10, 5]
n = 6
print(fetch_frequency(6,arr)) 

        