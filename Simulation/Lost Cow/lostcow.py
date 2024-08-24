in_ = open("Simulation/Lost Cow/lostcow.in", "r")
out_ = open("Simulation/Lost Cow/lostcow.out", "w")

x, y, = list(map(int, in_.readline().split()))
ans = 0
current = 1
while True:
    if current % 2 == 1:
        if x <= y <= x + current:
            ans += abs(y - x)
            break
        else:
            ans += current
            x += current
    else:
        if x >= y >= x - current:
            ans += abs(y - x)
            break
        else:
            ans += current
            x -= current
    current *= 2
out_.write(str(ans))