string = "MADAM"
temp = ""
i = 0

def check(string,temp,i):
    if i == len(string):
        if string == temp:
            return "Palindrome"
        else:
            return "Not Palindrome"
    else :
        temp = temp + string[len(string)-1-i]
        return check(string,temp,i+1)

result = check(string,temp,i)
print(result)