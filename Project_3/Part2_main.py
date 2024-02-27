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

## train on patterns
p1 = utils.get_random_pattern()
p2 = utils.get_random_pattern()
p3 = utils.get_random_pattern()
# print(p1)
network.train_on_pattern(p1)
network.train_on_pattern(p2)
network.train_on_pattern(p3)

## generate test pattern sets
ptts = [p1, p2, p3]
runs = 5
t0 = [[utils.get_flip_pattern(p, .0) for _ in range(runs)] for p in ptts]
t1 = [[utils.get_flip_pattern(p, .1) for _ in range(runs)] for p in ptts]
t2 = [[utils.get_flip_pattern(p, .2) for _ in range(runs)] for p in ptts]
t3 = [[utils.get_flip_pattern(p, .3) for _ in range(runs)] for p in ptts]
t4 = [[utils.get_flip_pattern(p, .4) for _ in range(runs)] for p in ptts]
t5 = [[utils.get_flip_pattern(p, .5) for _ in range(runs)] for p in ptts]

## run tests
times, hamming_distances, energies = utils.run_tests(network, t0, t1, t2, t3, t4, t5)
print("Part 2 tests")
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

## two more patterns
print("for the two more random patterns:")
p4 = utils.get_random_pattern()
network.train_on_pattern(p4)
t4 = [[utils.get_flip_pattern(p4, 0.2) for _ in range(5)]]
times4, hamming_distances4, energies4 = utils.run_tests(network, t4)
mean_times4 = utils.get_mean(times4)
print(times4[0][0], hamming_distances4[0][0], mean_times4)

p5 = utils.get_random_pattern()
network.train_on_pattern(p5)
t5 = [[utils.get_flip_pattern(p5, 0.2) for _ in range(5)]]
times5, hamming_distances5, energies5 = utils.run_tests(network, t5)
mean_times5 = utils.get_mean(times5)
print(times5[0][0], hamming_distances5[0][0], mean_times5)