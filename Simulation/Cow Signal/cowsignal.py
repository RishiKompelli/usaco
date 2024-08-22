import sys
sys.stdin = open("Cow Signal/cowsignal.in", "r")
sys.stdout = open("Cow Signal/cowsignal.out", "w")

m, n, k = map(int, input().split())
cowsignal = [input() for i in range(m)]
for b in cowsignal:
    d = [c for c in b]
    e = [f*k for f in d]
    for g in range(k):
        print(''.join(e))