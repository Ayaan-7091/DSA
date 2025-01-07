import math

n = int(input('Enter N : '))

# def checkPrime(n):
#     if n<=1 :
#         return "Not Prime"
#     for i in range(2,n+1):

#         if(n != i):
#             if(n % i == 0):
#                 return "Not Prime"
#     return "Prime"
    
# print(checkPrime(n))

# better approach

def checkPrime_b(n):

    count = 0

    for i in range(1,n+1):
        if(n % i == 0):
            count = count + 1

    if(count > 2):
        return "Not Prime"
    else:
        return "Prime"
    
# print(checkPrime_b(n))

# optimal approach

def checkPrime_op(n):
    count = 0

    for i in range(1,int(math.sqrt(n))+1):
        if(n%i==0):
            count = count + 1
            # If n is not a perfect square,
            # count its reciprocal factor.
            if n // i != i:
                count = count + 1
    
    if(count > 2):
        return "Not Prime"
    else:
        return "Prime"
    
print(checkPrime_op(n))