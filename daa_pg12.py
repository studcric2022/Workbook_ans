string1=['you','are','beautiful',"looking"]
n=len(string1)
for i in range(n):
    for j in range(i+1,n):
        temp=""
        if len(string1[i])>len(string1[j]):
            temp=string1[i]
            string1[i]=string1[j]
            string1[j]=temp

print(string1)


