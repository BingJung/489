from Connection import Connection
from Unit import Unit
from HopfieldNet import HopfieldNet
from itertools import permutations
import utils
import matplotlib.pyplot as plt

## implement the network
units = [Unit(0) for _ in range(16)]
conns_dict = {f"({i}, {j})" : Connection(units[i], units[j]) for i, j in permutations(range(16), 2)} # index of conn(i, j) in conns: i*4 + j
for i, j in permutations(range(16), 2):
    units[i].add_connection(conns_dict[f"({i}, {j})"])
    units[j].add_connection(conns_dict[f"({i}, {j})"])
network = HopfieldNet(units, conns_dict)
# print(len(conns_dict))
# for i in range(16):
#     print(len(units[i].incoming_connections))

# train on patterns
p1 = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
p2 = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]
p3 = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]
p4 = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
# print(len(p1))
network.train_on_pattern(p1)
network.train_on_pattern(p2)
network.train_on_pattern(p3)
network.train_on_pattern(p4)
# print([conn.weight for conn in conns_dict.values()])

## generate test pattern sets
ptts = [p1, p2, p3, p4]
runs = 5
t0 = [[utils.get_flip_pattern(p, .0) for _ in range(runs)] for p in ptts]
t1 = [[utils.get_flip_pattern(p, .1) for _ in range(runs)] for p in ptts]
t2 = [[utils.get_flip_pattern(p, .2) for _ in range(runs)] for p in ptts]
t3 = [[utils.get_flip_pattern(p, .3) for _ in range(runs)] for p in ptts]
t4 = [[utils.get_flip_pattern(p, .4) for _ in range(runs)] for p in ptts]
t5 = [[utils.get_flip_pattern(p, .5) for _ in range(runs)] for p in ptts]

# print(t1[0][0])
# times, hamming_dis, energies = network.run_to_settle(t1[0][0])
# print(network.get_pattern())
# # print(times)
# print(hamming_dis)
# # print(energies, len(energies))

## run tests
times, hamming_distances, energies = utils.run_tests(network, t0, t1, t2, t3, t4, t5)
print("times to settle:", times)
print("hamming distances after settled:", hamming_distances)

## get means
mean_times = []
for i in times:
    mean_l1 = []
    for j in i:
        mean_l1.append(sum(j) / len(j))
    mean_times.append(sum(mean_l1) / len(mean_l1))
print("mean times under each probability:", mean_times)

mean_hamming_distances = []
for i in hamming_distances:
    mean_l1 = []
    for j in i:
        mean_l1.append(sum(j) / len(j))
    mean_hamming_distances.append(sum(mean_l1) / len(mean_l1))
print("mean hamming distances under each probability:", mean_hamming_distances)

## plot energies
for i in energies:
    for j in i:
        for m in j:
            plt.plot(m)
plt.show()
