def reverse_array(num,rev):
    
    if(not num):
        return rev
    
    n = num.pop()
    rev.append(n)
    return reverse_array(num,rev)

num = [1,2,3,4,5]
rev = []
print(reverse_array(num,rev))