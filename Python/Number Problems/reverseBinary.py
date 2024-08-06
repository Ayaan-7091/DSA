# Problem statement
# There is a song concert going to happen in the city
# The price of each ticket is equal to the number obtained
# after reversing the bits of a given 32 bits unsigned integer ‘n’.


n = int(input("Enter N! : "))

binary_string = format(n,'032b')
reversed_binary = binary_string[::-1]

result = int(reversed_binary,2)

print(result)