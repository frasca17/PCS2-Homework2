import sys
tests = int(input())
for _ in range(tests):
    s = input()
    deletions = 0
    for letter in range(1, len(s)):
        if s[letter] == s[letter-1]:
            deletions = deletions + 1
    print (deletions)
