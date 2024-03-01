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

## get patterns and train
base = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
ps = [utils.get_flip_pattern(base, 0.125) for _ in range(6)]
for p in ps:
    network.train_on_pattern(p)

## run tests
ts = [[i for _ in range(5)] for i in ps]
times, hamming_distances, energies, states = utils.run_tests(network, ps, ts, get_states=True)
print("Part 3 tests")
print("times to settle:", times)
print("hamming distances after settled:", hamming_distances)
print("settled patterns:", states)

## get means
mean_times = utils.get_mean(times)
print("mean times for each pattern:", mean_times)

mean_hamming_distances = utils.get_mean(hamming_distances)
print("mean hamming distances for each pattern:", mean_hamming_distances)

# # uncomment to print, plot energy and save data
# print("energy:", energies)

# for i in energies:
#     for j in i:
#         for m in j:
#             plt.plot(m)
# plt.show()

# with open("Part3_energy.txt", "w") as file:
#     file.write(str(energies))
# with open("Part4_results.txt", "w") as file:
#     file.write("Part 3 tests\n")
#     file.write(f"\ntimes to settle:\n{str(times)}\n")
#     file.write(f"\nhamming distances after settled:\n{str(hamming_distances)}\n")
#     file.write(f"\nsettled patterns:\n{str(states)}\n")
#     file.write(f"\nmean times under each probability for each pattern:\n{str(mean_times)}\n")
#     file.write(f"\nmean hamming distances under each probability for each pattern:\n{str(mean_times)}\n")