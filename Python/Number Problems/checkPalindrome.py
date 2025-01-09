n = int(input("Enter N : "))

sample = n
reversed = 0

if(n<0):
    print("false")

while n>0:
    last_digit = n%10
    reversed = (reversed*10) + last_digit
    n = int(n/10)
print(reversed)
if(sample == reversed):
    print("true")
else:
    print("false")




