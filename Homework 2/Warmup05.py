import sys

N = int(input())
diag_difference = 0
for i in range(N):
    row = input().split()
    diag_difference += (int(row[i]) - int(row[N-1-i]))
print (abs(diag_difference))
 