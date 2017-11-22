size = int(input())
arr = list(map(int, input().split()))
for j in range(1, size):
    value = arr[j]
    for i in range(j, -1, -1):
        if i > 0 and arr[i-1] >= value:
            arr[i] = arr[i-1]
        else:
            arr[i] = value
            break
            
    print(" ".join(map(str, arr)))
    