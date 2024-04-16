from BPNet import BPNet

import matplotlib.pyplot as plt
import numpy as np

patterns1 = [[1, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 0]]

pattern2 = [0, 0, 0, 0, 0, 0, 0, 1]

patterns3 = [[1, 1, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 1, 1, 0, 0]]

p3_tests = [[0, 0, 1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 0, 0, 0]]

autoencoder = BPNet([8, 3, 8], 6)

print("epochs:", autoencoder.train_until_ok(patterns1, patterns1))
for p in patterns1:
    print(autoencoder.forward(p, bin=True))

print("test on last unit:", autoencoder.forward(pattern2, bin=True))

print("epochs:", autoencoder.train_until_ok(patterns3, patterns3))
# print("epochs:", autoencoder.train_until_ok(patterns1+patterns3, patterns1+patterns3, hard=True))
for p in patterns3:
    print(autoencoder.forward(p, bin=True))

for p in p3_tests:
    print("untrained tests:", autoencoder.forward(p, bin=True))

for p in patterns1:
    print("test on p1:", autoencoder.forward(p, bin=True))

print("test on last unit:", autoencoder.forward(pattern2, bin=True))