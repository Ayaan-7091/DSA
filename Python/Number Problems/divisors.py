import math
n = int(input("Enter N : "))

# for i in range(1,n+1):
#     if(n%i==0):
#         print(i)

# optimal approach
divisors = []

sqrt = int(math.sqrt(n))

for i in range(1,sqrt+1):
    
    if(n%i==0):
       divisors.append(i)
       
       if(i != n//i):
          divisors.append(n//i)

print(divisors)