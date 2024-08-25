N = int(input())
cows = []
for i in range(N):
    cows.append(int(input()))

minsteps = 1000000000

for i in range(N):
    steps = 0
    for j in range(N):
        steps += j * cows[(i + j) % N]
    minsteps = min(minsteps, steps)

print(minsteps)