import sys
sys.stdin = open("diamond collector/diamond.in", "r")
sys.stdout = open("diamond collector/diamond.out", "w")

n,k = [int(i) for i in input().split()]
weights = []
for i in range(n):
    weights.append(int(input()))

ans = 0
for i in range(n):
    amt = 0
    for j in range(n):
        if weights[j] >= weights[i] and weights[j] <= weights[i] + k:
            amt+=1
    if amt > ans:
        ans = amt

print(ans)