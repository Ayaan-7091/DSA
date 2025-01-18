def sum_n_numbers(n,sum):
    if(n>0):
        sum = sum + n
        sum_n_numbers(n-1,sum)
    else:
        print(sum)

n = int(input('Enter N : '))
sum_n_numbers(n,0)