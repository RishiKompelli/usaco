s = input()

pos = {}

for i in range(len(s)):
    if s[i] not in pos:
        pos[s[i]] = [i]
    else:
        pos[s[i]].append(i)
pair = 0
for i in range(len(pos.keys())):
    x = list(pos.items())[i]
    for j in range(i, len(pos.keys())):
        y = list(pos.items())[j]    
        if x != y:

            if x[1][0] < y[1][0] and x[1][1] > y[1][0] and x[1][1] < y[1][1]:
                pair += 1
                
print(pair)