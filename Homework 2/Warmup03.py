import sys

def solve(a0, a1, a2, b0, b1, b2):
    alice_score = 0
    bob_score = 0
    comparisons = zip([a0,a1,a2], [b0,b1,b2])
    for i in comparisons:
        if i[0]==i[1]:
            continue
        elif i[0] > i[1]:
            alice_score += 1
        else:
            bob_score += 1
    print(alice_score, bob_score)

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))
