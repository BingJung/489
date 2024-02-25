from Connection import Connection
from Unit import Unit
from HopfieldNet import HopfieldNet
from itertools import permutations

# implement the network
units = [Unit(0) for _ in range(16)]
conns_dict = {f"({i}, {j})" : Connection(units[i], units[j]) for i, j in permutations(range(16), 2)}
# index of conn(i, j) in conns: i*4 + j
for i, j in permutations(range(16), 2):
    units[i].add_connection(conns_dict[f"({i}, {j})"])
    units[j].add_connection(conns_dict[f"({i}, {j})"])
network = HopfieldNet(units, conns_dict)
# for i in range(16):
#     print(len(units[i].incoming_connections))

# train on patterns
p1 = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
# print(len(p1))
network.train_on_pattern(p1)
# for conn in conns_dict.values():
#     print(conn.weight)