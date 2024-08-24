import sys

sys.stdin = open('Simulation/Bucket List/blist.in','r')
sys.stdout = open('Simulation/Bucket List/blist.out','w')

N = int(input())
cows = [list(map(int,input().split())) for i in range(N)]

start_times = [cow[0] for cow in cows]
stop_times = [cow[1] for cow in cows]

availableB = 0
totalB = 0
for time in range(min(start_times),max(stop_times)):
    if time in stop_times:
        availableB += cows[stop_times.index(time)][2]
    if time in start_times:
        if cows[start_times.index(time)][2] < availableB:
            availableB -= cows[start_times.index(time)][2]
        else:
            totalB += cows[start_times.index(time)][2] - availableB
            availableB = 0
    
print(totalB)