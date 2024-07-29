n = int(input("Enter N \n"))
k=0
for i in range(0,n):
    for j in range(n-i,0,-1):
        k+=1
        print(k,end=" ")
    print()
    k=0