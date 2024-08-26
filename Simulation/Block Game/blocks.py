import sys
sys.stdin = open("blocks.in", "r")
sys.stdout = open("blocks.out", "w")
def frequency(s):
  freqs = [0] * 26
  for c in s:
    freqs[ord(c) - ord('a')] += 1
  return freqs
N = int(input())
res = [0] * 26
for _ in range(N):
    s1, s2 = input().split()
    freq1 = frequency(s1)
    freq2 = frequency(s2)
    for i in range(26):
        res[i] += max(freq1[i], freq2[i])
for freq in res:
  print(freq)