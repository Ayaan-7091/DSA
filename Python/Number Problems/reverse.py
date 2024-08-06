import numpy

n = int(input("Enter N! : "))

reversed = 0
sign = 1
if(n<0):
    sign = -1

n = numpy.abs(n)


while(n>0):
    lastDigit = n%10
    reversed = (reversed * 10) + lastDigit
    n = int(n/10)

print(reversed*sign)