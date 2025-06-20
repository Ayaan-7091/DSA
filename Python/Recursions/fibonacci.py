# n = 5
# n = n - 3 # to avoid the const 0 and 1
# i = 0
# f = [0,1]

# def fib(n,i,f):
#     size = len(f)
#     if(i<=n):
#         f.append(f[size-1] + f[size-2])
#         return fib(n,i+1,f)
    
#     return f

# print(fib(n,i,f))

# OPTIMAL SOLUTION -->

def fib(n, f=None):
    if f is None:
        f = [0,1]
    
    if len(f) >= n:
        return f[:n]
    f.append(f[-1] + f[-2])
    return fib(n,f)
n = 5
print(fib(n))