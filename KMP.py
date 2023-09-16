def search(t, p):
    m = len(p)
    n = len(t)
    arr = [0] * m
    arr[0] = 0
    i, j = 1, 0

    while i < m:
        if p[i] == p[j]:
            j += 1
            arr[i] = j
            i += 1
        else:
            if j != 0:
                j = arr[j - 1]
            else:
                arr[i] = 0
                i += 1

    found = False
    i = j = 0
    while i < n:
        if t[i] == p[j]:
            i += 1
            j += 1
            if j == m:
                found = True
                print("Pf", i - m)
                j = arr[j - 1]
        else:
            if j != 0:
                j = arr[j - 1]
            else:
                i += 1

    if not found:
        print("pnf")

def main():
    t = "AABAACAADAABAAB A"
    p = "AABA"
    search(t, p)

if __name__ == "__main__":
    main()
