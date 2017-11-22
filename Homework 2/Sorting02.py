value = int(input())
n = int(input())
ar = map(int, input().split())
#print(list(ar).index(value))

for k, v in enumerate(ar):
    if v== value:
        print(k)
        break# in case we find the value before the end of the for cycle