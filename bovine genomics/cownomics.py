import sys

sys.stdin = open("bovine genomics/cownomics.in", "r")
sys.stdout = open("bovine genomics/cownomics.out", "w")

N, M = map(int, input().split())

spots = []
plains = []
for _ in range(N):
    spots.append(list(input()))

for _ in range(N):
    plains.append(list(input()))


count = 0
for i in range(M):
    is_potential = True
    spot_c = set()
    plain_c = set()
    for j in range(N):
        spot_c.add(spots[j][i])
        plain_c.add(plains[j][i])
    
    for val in spot_c:
        if val in plain_c:
            is_potential = False
            break
    
    if is_potential:
        count += 1
print(count, end="")