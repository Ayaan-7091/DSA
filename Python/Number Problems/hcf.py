n1 = int(input("Enter n1 : "))
n2 = int(input("Enter n2 : "))


hcf = 1

n_range = n1 if n1>n2 else n2
for i in range(1,n_range):
    if(n1 % i == 0 and n2 % i == 0):
        hcf = i
print(hcf)
