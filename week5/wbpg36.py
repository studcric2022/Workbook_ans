t=int(input("Enter No. of Testcases"))
while t>0:
    l1=[]
    r=False
    n=int(input("enter size of array"))
    for i in range(n):
        l1.append(int(input()))
    for i in range(n):
        if sum(l1[0:i])==sum(l1[i+1:n]):
            r = True

    if r:
        print("yes")
    else:
        print("no")

    t=t-1