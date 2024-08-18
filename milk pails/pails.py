import sys

sys.stdin = open("pails/pails.in", 'r')
sys.stdout = open("pails/pails.out", 'w')

X, Y, M = map(int, input().split())

diff = 1000

for n in range(M // X + 1):
    diff = min(diff, (M - (X * n)) % Y)

print (M - diff)