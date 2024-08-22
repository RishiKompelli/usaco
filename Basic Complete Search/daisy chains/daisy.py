n = int(input())
flowers = [int(x) for x in input().split()]
count = 0
for j in range(1, n+1):
   for i in range(0,n-(j-1)):
       sub = flowers[i:i+j]
       if sum(sub)/len(sub) in sub:
           count +=1
print(count)