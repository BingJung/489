# requirement: customizing learning rate, momentum

from typing import Sequence
from Connection import Connection
from Unit import Unit

from itertools import product, pairwise

from IPython import embed

class BPNet:
    def __init__(self, units_nums: Sequence, learning_rate = 0.5, momentum = 0) -> None:
        # assuming all units are connecting each other without checking here
        # assuming connections: conns["(i, j)": Connection]
        self.units = [[Unit() for _ in range(num)] for num in units_nums]
        self.layer_num = len(units_nums) - 1
        self.unit_nums = units_nums
        self.learning_rate = learning_rate
        self.momentum = momentum
        self.weight_change = 0
        self.training_patterns = []

        # build connections and add to units
        self.connections_forward = [{f"({unit1}, {unit2})" : Connection(self.units[layer][unit1], self.units[layer+1][unit2]) for unit1, unit2 in product(range(units_nums[layer]), range(units_nums[layer+1]))} for layer in range(self.layer_num)]

        for layer1, layer2 in pairwise(range(self.layer_num + 1)):
            for unit1, unit2 in product(range(units_nums[layer1]), range(units_nums[layer2])):
                self.units[layer1][unit1].add_connection(self.connections_forward[layer1][f"({unit1}, {unit2})"])
                self.units[layer2][unit2].add_connection(self.connections_forward[layer1][f"({unit1}, {unit2})"])

    # forward activation
    def forward(self, pattern: Sequence) -> list: 
        assert len(pattern) == self.unit_nums[0], f"input size is supposed to be {self.unit_nums[0]}"
        # set activations in the first layer; inputs are not set
        for i in range(len(pattern)):
            self.units[0][i].set_activation(pattern[i])
        for layer_id, layer in enumerate(self.units):
            if layer_id == 0:
                continue
            for unit in layer:
                unit.get_input()
                unit.update_activation()
        return [unit.get_activation() for unit in self.units[-1]]

    # backward error
    def backward(self, target: Sequence):
        assert len(target) == self.unit_nums[-1], f"input size is supposed to be {self.unit_nums[-1]}"
        # update errors in the last error
        for id, unit in enumerate(self.units[-1]):
            unit.update_unit_error(target[id])

        # back propagates errors
        for layer in reversed(self.units[:-1]):
            for unit in layer:
                unit.sum_forward_error()

    # update weights according to errors
    def update_weights(self):
        for weight_layer in self.connections_forward:
            for conn in weight_layer.values():
                conn.update_weight(self.learning_rate, self.momentum)

    # train on pattern once
    def train_on_pattern(self, pattern: Sequence, target: Sequence) -> list:
        # train
        self.forward(pattern)
        self.backward(target)
        self.update_weights()

        # add to self.training_pattern and return output
        self.training_patterns.append((pattern, target))
        return self.forward(pattern)

    def test_on_pattern(self, pattern: Sequence, target: Sequence) -> list:
        self.forward(pattern)
        return [i == (j > 0.5) for i, j in zip(target, self.get_output())]
    
    # train the net work on a set of pattern until it generates the correct output

    def set_learning_rate(self, learning_rate):
        self.learning_rate = learning_rate

    def set_momentum(self, momentum):
        self.momentum = momentum

    def get_output_error(self, )
    # get global error
    def get_G(self, patterns, target) -> float:
        G = 0
        for pattern in patterns:
            pass
    ### TODO 

    def get_output(self) -> list:
        return [unit.get_activation() for unit in self.units[-1]]
    
    def get_training_patterns(self) -> list:
        return self.training_patterns

    def init_weights(self):
        for conn in self.conns_dict.values:
            conn.init_weight()
        self.training_patterns = []


    
