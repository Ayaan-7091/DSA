# string = "MADAM"
# temp = ""
# i = 0

# def check(string,temp,i):
#     if i == len(string):
#         if string == temp:
#             return "Palindrome"
#         else:
#             return "Not Palindrome"
#     else :
#         temp = temp + string[len(string)-1-i]
#         return check(string,temp,i+1)

# result = check(string,temp,i)
# print(result)

# OPTIMAL SOLUTION -->

def is_palindrome(string, start, end):
    if start >= end:
        return "Palindrome"
    
    if string[start] != string[end]:
        return "Not Palindrome"
    
    return is_palindrome(string, start+1, end - 1)

string = "MADAM"
print(is_palindrome(string, 0, len(string)-1))