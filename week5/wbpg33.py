list1=[]
list2=[]
n=int(input())
m= int(input())
for i in range(n):
    list1.append(int(input()))
for j in range(m):
    list2.append(int(input()))
#x= set(list1)&set(list2)
#y=set(list2)-x
#print(y)
z=0
for i in range(n):
    z=list1[i]
    list2.remove(z)

print(list2)