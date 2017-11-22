from collections import Counter
s = input().lower()
if len(Counter(s)) == 27:
    print("pangram")
else:
    print("not pangram")
