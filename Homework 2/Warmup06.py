import sys
from decimal import *
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

positive = 0
negative = 0
zero = 0

for i in arr:
    if (i > 0):
        positive = positive + 1

    elif (i < 0):
        negative = negative + 1

    else:
        zero = zero + 1

pos_fraction = Decimal(positive) / Decimal(n)
result1 = format(pos_fraction, '.6f')
print(result1)

neg_fraction = Decimal(negative) / Decimal(n)
result2 = format(neg_fraction, '.6f')
print(result2)

zero_fraction = Decimal(zero) / Decimal(n)
result3 = format(zero_fraction, '.6f')
print(result3)
