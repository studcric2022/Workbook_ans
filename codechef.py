t=int(input())
list1=[]
list2=[]
def small_nm():

while t<=10:
    n=int(input())
    for i in range(n):
        list1.append(int(input()))

    for i in range(n):
        for j in range(i+1,n):
            list2.append(list1[i] - list1[j])





    t=t-1

