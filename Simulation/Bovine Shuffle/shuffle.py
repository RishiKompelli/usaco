import copy
in_ = open('Simulation/Bovine Shuffle/shuffle.in','r')
out_ = open('Simulation/Bovine Shuffle/shuffle.out','w')
data = in_.read().splitlines()
n = int(data[0])
shuffle_positions = list(map(int, data[1].split(' ')))
ids = list(map(int, data[2].split(' ')))
print(ids)

for iteration in range(3):
    old_positions = [0] * len(ids)
    print(shuffle_positions)
    for index, i in enumerate(shuffle_positions):
        old_positions[index] = copy.copy(ids[i-1])
    ids = copy.copy(old_positions)
    print(ids)
    
out_.write(''.join([str(i) + '\n' for i in ids]))