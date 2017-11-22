import sys


s = input().strip()
words = 1
for character in s:
    if character.isupper():
        words = words + 1
print (words)
