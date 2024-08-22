import sys
sys.stdin = open("balancing.in", "r")
sys.stdout = open("balancing.out", "w")

n = int(input().split()[0])
xLoc = []
yLoc = []
for _ in range(n):
	inp = [int(i) for i in input().split()]
	xLoc.append(inp[0])
	yLoc.append(inp[1])
ans = n

for xIndex in range(n):
	for yIndex in range(n):
		xDiv = xLoc[xIndex]+1
		yDiv = yLoc[yIndex]+1
		upperLeft = 0
		upperRight = 0
		lowerLeft = 0
		lowerRight = 0
		for i in range(n):
			if xLoc[i] < xDiv and yLoc[i] < yDiv:
				lowerLeft+=1
			if xLoc[i] < xDiv and yLoc[i] > yDiv:
				upperLeft+=1
			if xLoc[i] > xDiv and yLoc[i] < yDiv:
				lowerRight+=1
			if xLoc[i] > xDiv and yLoc[i] > yDiv:
				upperRight+=1
		worstRegion = max(upperLeft,upperRight,lowerLeft,lowerRight)
		if worstRegion < ans:
			ans = worstRegion
print(ans)