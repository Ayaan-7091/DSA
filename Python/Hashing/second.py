array = [1,2,3,1,4,1,5,2,1]

n = int(input("Check the Appearance Frequency: "))

hash = [0,0,0,0,0,0,0,0,0,0,0,0,0]

def fetch_frequency(n,array):
    for i in range (0,len(array)):
        hash[array[i]] += 1
    return hash[n]

print(fetch_frequency(n,array))

      