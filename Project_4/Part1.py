# requirements: (1 layer + 2 layer) * 3 pattern sets * parameter space (learning rate, momentum)
# experiment 2: add noise
from BPNet import BPNet
from Patterns import *

import matplotlib.pyplot as plt
import numpy as np
import random

set1 = (patterns_1, targets4)
set2 = (patterns_2, targets4)
set3 = (patterns_3, targets2)

# testing epochs needed under different learning rates
def test_lr(set):
    learning_rates = np.linspace(0.1, 40, 30)
    epochs1 = []
    epochs2 = []
    for l in learning_rates:
        network = BPNet([10, 4], l)
        epochs1.append(network.train_until_ok(*set))

    for l in learning_rates:
        network = BPNet([10, 6, 4], l)
        epochs2.append(network.train_until_ok(*set))

    _, ax = plt.subplots(1, 2, figsize=(8,4))
    ax[0].plot(learning_rates, epochs1)
    ax[0].set_title("network1")
    ax[1].plot(learning_rates, epochs2)
    ax[1].set_title("network2")
    plt.show()

# testing epochs need under different momentums
def test_m(set):
    momentums = np.linspace(0, 0.95, 15)
    epochs1 = []
    epochs2 = []
    for m in momentums:
        network = BPNet([10, 4], 8, m)
        epochs1.append(network.train_until_ok(*set))

    for m in momentums:
        network = BPNet([10, 6, 4], 2.1, m)
        epochs2.append(network.train_until_ok(*set))

    _, ax = plt.subplots(1, 2, figsize=(8,4))
    ax[0].plot(momentums, epochs1)
    ax[0].set_title("network1")
    ax[1].plot(momentums, epochs2)
    ax[1].set_title("network2")
    plt.show()

# testing error rate on noisy versions of original data
def test_g(set):
    # train
    network1 = BPNet([10, 4], 8)
    network2 = BPNet([10, 6, 4], 2.2)
    network1.train_until_ok(*set)
    network2.train_until_ok(*set)

    # test
    probs = np.linspace(0, 1, 52)
    errors1 = []
    errors2 = []
    # iterate through probs
    for prob in probs:
        distirbed = set[0].copy()
        # add noise
        for i in distirbed:
            for j in range(len(i)):
                if random.random() > prob:
                    continue
                # flip
                if i[j] == 1:
                    i[j] = 0
                else:
                    i[j] = 1
        # sum outputs
        errors1.append(1 - sum([sum(network1.test_on_pattern(i, j)) for i, j in zip(distirbed, set[1])]) / sum([len(o) for o in set[1]]))
        errors2.append(1 - sum([sum(network2.test_on_pattern(i, j)) for i, j in zip(distirbed, set[1])]) / sum([len(o) for o in set[1]]))

    _, ax = plt.subplots(1, 2, figsize=(8,4))
    ax[0].plot(probs, errors1)
    ax[0].set_title("network1")
    ax[1].plot(probs, errors2)
    ax[1].set_title("network2")
    plt.show()
        
network = BPNet([10, 6, 4], 3)
print(network.train_until_ok(*set1))

# test_g(set3)

# for p in patterns_1:
#     print(network.forward(p))