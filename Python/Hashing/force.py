array = [1,2,3,1,4,1,5,2,1]

# print(len(array))

n = int(input("Check the Appearance Frequency: "))
count = 0

for i in range(0,len(array)) :
    if n == array[i]:
        count = count + 1

print(f"{n} appears for - {count} times")

