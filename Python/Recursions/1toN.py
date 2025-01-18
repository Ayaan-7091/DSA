def print1ToN(n,count):
    n = n - 1
    count = count + 1

    if(n>=0):
        print(count)
        print1ToN(n,count)
    else:
        return

n = int(input('Enter N :'))
print1ToN(n,0)