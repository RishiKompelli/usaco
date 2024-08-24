import sys
sys.stdin = open('Simulation/Speeding Ticket/speeding.in', 'r')
sys.stdout = open('Simulation/Speeding Ticket/speeding.out', 'w')
N, M = map(int, input().split())
road, drive = [], []
for _ in range(N):
    length, limit = map(int, input().split())
    road.extend([limit] * length)
for _ in range(M):
    length, speed = map(int, input().split())
    drive.extend([speed] * length)
ans = 0
for i in range(100):
    dif = drive[i] - road[i]
    ans = max(dif, ans)
print(ans)