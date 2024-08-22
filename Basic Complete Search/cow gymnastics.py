n, k = map(int, input().split())
gym = []
for i in range(n):
    lists = list(map(int, input().split()))
    gym.append(lists)

counter = 0
for j in range(1, k+1):
    for l in range(1, k+1):
        count = 0
        for i in range(n):
            if gym[i].index(j) > gym[i].index(l):
                count += 1
        if count == n:
            counter += 1

print(counter)