a, b, x, y = map(int, input().strip().split())
distance = abs(a-b)
distance_teleporter_1 = abs(a - x) + abs(y - b)
distance_teleporter_2 = abs(a - y) + abs(x - b)
min_distance = min(distance, distance_teleporter_1, distance_teleporter_2)
print(min_distance)