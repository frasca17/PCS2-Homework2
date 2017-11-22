N_rocks = int(input())

rocks = list(set(input()) for _ in range(N_rocks))
gem_elements = set.intersection(*rocks)
gems = len(gem_elements)
print(gems)

