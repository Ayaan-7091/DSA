# import numpy
n = int(input("Enter N : "))

digits = 0

while(n>0):
    last_digit = n % 10
    
    n = int(n/10)
   
    digits = digits + 1


# METHOD - 02

# digits = int(numpy.log10(n)+1)
print("The Number of digits : ",digits)


