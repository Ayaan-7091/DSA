n = int(input("Enter N!"))

str = str(n)

length = len(str)
if(length%2 != 0 ):
    print("false")

half_length = length//2

first_half = int(str[:half_length])
second_half= int(str[half_length:])

if(first_half == second_half):
    print(f"True as: {first_half} = {second_half}")
else:
    print(f"False as: {first_half} != {second_half}")


