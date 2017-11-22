import sys
from collections import defaultdict

n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
   unsorted_t = str(input().strip())
   unsorted.append(unsorted_t)
# your code goes here
dc = defaultdict(list)
for i in unsorted:
    dc[len(i)].append(i)
for k in sorted(dc):
    for v in sorted(dc[k]):
        print(v)