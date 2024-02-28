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

## get patterns and train
base = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
ps = [utils.get_flip_pattern(base, 0.125) for _ in range(6)]
for p in ps:
    network.train_on_pattern(p)

## run tests
ts = [[i for _ in range(5)] for i in ps]
times, hamming_distances, energies = utils.run_tests(network, ts)
print("Part 3 tests")
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