size = int(input())
arr = list(map(int, input().split()))
value = arr[size-1]
stop = False
for i in range(size - 1, -1, -1):
    if i > 0 and arr[i-1] >= value:
        arr[i] = arr[i-1]# we copy the number before of our current value
    else:
        arr[i] = value
        stop = True
    print(" ".join(map(str, arr)))
    if stop:
        break # we use break because we could have found the right position before the end of the cycle
        