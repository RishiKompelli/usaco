import sys
sys.stdin = open('Speeding Ticket/speeding.in', 'r')
sys.stdout = open('Speeding Ticket/speeding.out', 'w')
N, M = map(int, input().split())
road = []
drive = []
for i in range(N):
    length, speedlimit = map(int, input().split())
    road.extend([speedlimit]*length)
for i in range(M):
    length, speed = map(int, input().split())
    drive.extend([speed]*length)
answer = 0
for i in range(100):
    dif = drive[i] - road[i]
    ans = max(dif, answer)
print(answer)