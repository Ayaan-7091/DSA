n1 = int(input("Enter n1 : "))
n2 = int(input("Enter n2 : "))

# brute force approach

# hcf = 1

# n_range = n1 if n1>n2 else n2
# for i in range(1,n_range):
#     if(n1 % i == 0 and n2 % i == 0):
#         hcf = i
# print(hcf)

# better approach

# def hcf(n1,n2):
#     for i in range(min(n1,n2),0,-1):
#         if(n1 % i == 0 and n2 % i == 0):
#             return i
#     return 1

# print(hcf(n1,n2))

# optimal approach

# def hcf_op(n1,n2):

#     while(n1>0 and n2>0):
#         if(n1>n2):
#             n1 = n1-n2
#         else:
#             n2 = n2-n1
#     return max(n1,n2)

# print(hcf_op(n1,n2))

# optimal approach 2

def hcf_op_2(n1,n2):

    while(n1>0 and n2>0):
        if(n1>n2):
            n1 = n1 % n2
        else:
            n2 = n2 % n1
    
    if n1 == 0:
        return n2
    
    return n1

print(hcf_op_2(n1,n2))