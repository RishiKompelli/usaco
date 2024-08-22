try:
    N = int(input())
except:
    print('Invalid number of cows, expected integer')
    exit()
G = []
L = []
for i in range(N):
    j = input().split()
    if j[0] == 'G':
        G.append(int(j[1]))
    elif j[0] == 'L':
        L.append(int(j[1]))
    else:
        print('Invalid input')
G.sort()
L.sort()
liars = 0
for i in range(len(L)):
    for j in range(len(G)):
        if L[i] < G[j]:
            liars += 1
            break
print(liars)