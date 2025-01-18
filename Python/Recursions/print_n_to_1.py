def print_n_to_1(n):
    if(n>0):
        print(n)
        n = n - 1
        printNto1(n)
    else:
        return

n = int(input('Enter N : '))    
print_n_to_1(n)
