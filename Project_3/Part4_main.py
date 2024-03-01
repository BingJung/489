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
# change the "sync" values to control synchronization
sync = 4
times, hamming_distances, energies = utils.run_tests(network, ptts, t0, t1, t2, t3, t4, t5, sync=sync)
print("Part 4 tests")
print("times to settle:", times)
print("hamming distances after settled:", hamming_distances)

## get means
mean_times = utils.get_mean(times)
# for i in range(len(mean_times)):
#     if None not in mean_times[i]:
#         mean_times[i] = sum(mean_times[i])
#     else:
#         mean_times[i] = None
print("mean times under each probability for each pattern:", mean_times)

mean_hamming_distances = utils.get_mean(hamming_distances)
# for i in range(len(mean_hamming_distances)):
#     if None not in mean_hamming_distances[i]:
#         mean_hamming_distances[i] = sum(mean_hamming_distances[i])
#     else: mean_hamming_distances[i] = None
print("mean hamming distances under each probability for each pattern:", mean_hamming_distances)

# ## uncomment to save data
# with open("Part4_energy.txt", "a") as file:
#     file.write(f"energy states when updating {sync} unit(s) each iteration:\n{str(energies)}\n")
# with open("Part4_results.txt", "a") as file:
#     file.write(f"\nupdating {sync} unit(s) each iteration:\n")
#     file.write(f"times to settle:\n{str(times)}\n")
#     file.write(f"hamming distances after settled:\n{str(hamming_distances)}\n")
#     file.write(f"mean times under each probability for each pattern:\n{str(mean_times)}\n")
#     file.write(f"mean hamming distances under each probability for each pattern:\n{str(mean_times)}\n")

# for i in energies:
#     for j in i:
#         for m in j:
#             plt.plot(m)
# plt.show()