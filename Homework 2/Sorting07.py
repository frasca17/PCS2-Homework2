n = int(input())
arr = list(map(int, input().split()))

def partition(l, p, r):
    pivot = l[p]
    i = p
    j = r
    while(True):
        while(l[i] < pivot and l[i] != pivot):#left side
            i += 1
        while(l[j] > pivot and l[j] != pivot):
            j -= 1
        if(i < j):
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
        else:
            return j
partition(arr, 0, n-1)
print(" ".join(map(str, arr)))
