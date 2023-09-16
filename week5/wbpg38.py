def merge_sort(arr):
    if len(arr) <= 1:
        return arr


    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]


    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)


    merged = merge(left_half, right_half)
    print(f'Merging: {left_half} and {right_half} => {merged}')

    return merged

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result


n= int(input("Enter Size of Array"))
arr=[]
for i in range(n):
    arr.append(int(input()))

sorted_arr = merge_sort(arr)
print("Sorted Array:", sorted_arr)
