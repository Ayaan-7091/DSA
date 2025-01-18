def sum_n_numbers(n,sum):
    if(n>0):
        sum = sum + n
        sum_n_numbers(n-1,sum)
    else:
        print(sum)

n = int(input('Enter N : '))
# sum_n_numbers(n,0)

# optimal approach

def sum_n_numbers_op(n):
    if(n==0):
        return 0
    else:
        return n + sum_n_numbers_op(n-1)

print(sum_n_numbers_op(n))