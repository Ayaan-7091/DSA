def print_n_times(n):
    if n>0:
        n = n - 1
        print('Hello World !')
        print_n_times(n)



# print_n_times(5)

# another approach
def print_n_times_v02(i,n):
    if i>n : return
        
    print('Hello World !')
    print_n_times_v02(i+1,n)

n = 5
print_n_times_v02(1,n)