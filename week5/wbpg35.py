t=int(input("Enter No. of Testcases"))
while t>0:
    l1=[]
    n=int(input("enter size of array"))
    for i in range(n):
        l1.append(int(input()))
    l1.sort()
    k=l1[n-1]
    if k%2==0:
        print(k+2)
    else:
        print(k+1)

    t=t-1