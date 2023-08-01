arr = [10, 23, 44, 12, 34, 22, 11, 10, 26, 12]
arr = sorted(arr)
low = 0
high = len(arr) - 1
x = 11
while low <= high:
    mid = (low + high) // 2
    if low >= high:
        print("No Element")
        break
    elif arr[mid] == x:
        print("X is Present On Index: ", mid)
        break
    elif arr[mid] < x:
        low = mid + 1
    elif arr[mid] > x:
        high = mid - 1
    else:
        print("No Element")






