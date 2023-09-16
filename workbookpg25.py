text = input("Enter text: ")
n = len(text)
pat = input("Pattern: ")
m = len(pat)
for i in range(n - m + 1):
    j = 0
    while j < m and text[i + j] == pat[j]:
        j += 1
    if j == m:
        print("Pattern found at index:", i)






