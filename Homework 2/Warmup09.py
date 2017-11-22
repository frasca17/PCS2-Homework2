import sys

       
n = int(input().strip())
candle_height = list(map(int, input().strip().split(' ')))

print(candle_height.count(max(candle_height)))

