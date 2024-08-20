import sys

sys.stdin = open("triangles/triangles.in", 'r')
sys.stdout = open("triangles/triangles.out", 'w')

n = int(input())
coords = []
for i in range(n):
  coords += [list(map(int, input().split()))]
area = 0

for a in coords:
  for b in coords:
    for c in coords:
      if a[0] == b[0] and a[1] == c[1]:
        area = max(area, abs(a[1] - b[1])*abs(a[0] - c[0]))
print(area)