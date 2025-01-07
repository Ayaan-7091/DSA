n1 = int(input('Enter N : '))

# sample = n1
# n2 = n1
# sum = 0
# count = 0

# while(n1>0):
#     last_digit = n1 % 10
#     n1 = int(n1/10)   
#     count = count + 1

# while(n2>0):
#     last_digit = n2 % 10
#     n2 = int(n2/10)
#     sum = sum + pow(last_digit,count)

# print(sum)

# approach - 2
n = n1

k = len(str(n))

sum = 0

while n>0:
    ld = n% 10
    sum = sum + ld**k
    n = n//10

if(sum == n1):
    print('Number is Amstrong')
else:
    print('Number is not Amstrong')
