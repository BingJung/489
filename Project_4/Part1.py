# requirements: (1 layer + 2 layer) * 3 pattern sets * parameter space (learning rate, momentum)
# experiment 2: add noise
from BPNet import BPNet
from Patterns import *

import matplotlib.pyplot as plt
from IPython import embed

# network = BPNet([10, 4], 5)
network = BPNet([10, 6, 4], 0.5)

print("epochs:", network.train_until_ok(patterns_1, targets4))
print(network.Gs)

# embed()

for p in patterns_1:
    print(network.forward(p))