# requirements: (1 layer + 2 layer) * 3 pattern sets * parameter space (learning rate, momentum)
# experiment 2: add noise

from BPNet import BPNet

network = BPNet([3, 2], 1, 0.2)

for _ in range(10):
    print(network.forward([1, 1, 1]))
    print(network.train_on_pattern([1, 1, 1], [0, 0]))
    print(network.test_on_pattern([1, 1, 1], [0, 0]))
