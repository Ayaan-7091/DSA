n  = [1,2,3,4,5]
a = []
def reverse(n,a):
    size = len(n)
    

    if size>0:
        a.append(n[size-1])
        n.pop()
        reverse(n,a)
    return a

print(reverse(n,a))
