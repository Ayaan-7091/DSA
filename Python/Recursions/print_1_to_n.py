def print_1_to_n(n,count):
    n = n - 1
    count = count + 1

    if(n>=0):
        print(count)
        print_1_to_n(n,count)
    else:
        return

n = int(input('Enter N :'))
print_1_to_n(n,0)