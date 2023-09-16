text=input()
n=len(text)
list1=[]
for i in range(n):
    list1.append(text[i])
pat=input()
m= len(pat)
list1=[]
for j in range(m):
    list1.append(pat[j])
mod= 21
sum=0
for i in range(m):
    sum=sum+int(pat[i])
print(sum)
#not able to done try again
