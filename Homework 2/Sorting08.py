from collections import defaultdict
n = int(input())
arr = list(map(int, input().split()))
dc = defaultdict(lambda: 0)

for i in arr:
    dc[i] += 1
print(" ".join(map(str, (dc[i] for i in range(0, 100)))))