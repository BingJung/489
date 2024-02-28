from Connection import Connection
from Unit import Unit
from HopfieldNet import HopfieldNet
from itertools import permutations
import utils
# import matplotlib.pyplot as plt

## implement the network
units = [Unit(0) for _ in range(16)]
conns_dict = {f"({i}, {j})" : Connection(units[i], units[j]) for i, j in permutations(range(16), 2)} # index of conn(i, j) in conns: i*4 + j
for i, j in permutations(range(16), 2):
    units[i].add_connection(conns_dict[f"({i}, {j})"])
    units[j].add_connection(conns_dict[f"({i}, {j})"])
network = HopfieldNet(units, conns_dict)  

## train on patterns
p1 = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
p2 = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]
p3 = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]
p4 = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
# print(len(p1))
network.train_on_pattern(p1)
network.train_on_pattern(p2)
network.train_on_pattern(p3)
network.train_on_pattern(p4)

## generate test pattern sets
ptts = [p1, p2, p3, p4]
runs = 5
t0 = [[utils.get_flip_pattern(p, .0) for _ in range(runs)] for p in ptts]
t1 = [[utils.get_flip_pattern(p, .1) for _ in range(runs)] for p in ptts]
t2 = [[utils.get_flip_pattern(p, .2) for _ in range(runs)] for p in ptts]
t3 = [[utils.get_flip_pattern(p, .3) for _ in range(runs)] for p in ptts]
t4 = [[utils.get_flip_pattern(p, .4) for _ in range(runs)] for p in ptts]
t5 = [[utils.get_flip_pattern(p, .5) for _ in range(runs)] for p in ptts]

## run tests
times, hamming_distances, energies = utils.run_tests(network, t0, t1, t2, t3, t4, t5, sync=16)
print("Part 4 tests")
print("times to settle:", times)
print("hamming distances after settled:", hamming_distances)

## get means
mean_times = utils.get_mean(times)
print("mean times under each probability:", mean_times)

mean_hamming_distances = utils.get_mean(hamming_distances)
print("mean hamming distances under each probability:", mean_hamming_distances)

# ## plot energies
# for i in energies:
#     for j in i:
#         for m in j:
#             plt.plot(m)
# plt.show()