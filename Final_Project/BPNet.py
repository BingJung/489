# requirement: customizing learning rate, momentum
from typing import Sequence
from Connection import Connection
from Unit import Unit

from itertools import product, pairwise

class BPNet:
    def __init__(self, units_nums: Sequence, learning_rate = 0.5, momentum = 0) -> None:
        # assuming all units are connecting each other without checking here
        # assuming connections: conns["(i, j)": Connection]
        self.units = [[Unit() for _ in range(num)] for num in units_nums]
        self.layer_num = len(units_nums) - 1
        self.unit_nums = units_nums
        self.learning_rate = learning_rate
        self.momentum = momentum
        self.Gs = [] # global errors; only modified by train_until_settle

        # build connections and add to units
        self.connections_forward = [{f"({unit1}, {unit2})" : Connection(self.units[layer][unit1], self.units[layer+1][unit2]) for unit1, unit2 in product(range(units_nums[layer]), range(units_nums[layer+1]))} for layer in range(self.layer_num)]

        for layer1, layer2 in pairwise(range(self.layer_num + 1)):
            for unit1, unit2 in product(range(units_nums[layer1]), range(units_nums[layer2])):
                self.units[layer1][unit1].add_connection(self.connections_forward[layer1][f"({unit1}, {unit2})"])
                self.units[layer2][unit2].add_connection(self.connections_forward[layer1][f"({unit1}, {unit2})"])

    # forward activation
    def forward(self, pattern: Sequence, bin = False) -> list: 
        assert len(pattern) == self.unit_nums[0], f"input size is supposed to be {self.unit_nums[0]} rather than {len(pattern)}"
        # set activations in the first layer; inputs are not set
        for i in range(len(pattern)):
            self.units[0][i].set_activation(pattern[i])

        # update the rest layers
        for layer_id, layer in enumerate(self.units):
            if layer_id == 0:
                continue
            for unit in layer:
                unit.get_input()
                unit.update_activation()

        if bin: # return binary outputs
            return [1 if unit.get_activation() > 0.5 else 0 for unit in self.units[-1]]
        else:
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
    def update_weight_changes(self, learning_rate):
        for weight_layer in self.connections_forward:
            for conn in weight_layer.values():
                conn.update_weight_change(learning_rate)

    def update_weights(self, momentum):
       for weight_layer in self.connections_forward:
            for conn in weight_layer.values():
                conn.update_weight(momentum) 

    # test on one pattern
    def test_on_pattern(self, pattern, target, return_error = False) -> list:
        # output = self.forward
        if return_error:
           return [(i - j)**2 for i, j in zip(target, self.forward(pattern))] 
        return [i == (j > 0.5) for i, j in zip(target, self.forward(pattern))]
    
    # train the net work on a set of patterns until it generates the correct output for all inputs
    def train_until_ok(self, patterns: Sequence, targets: Sequence, hard = False):
        epoch = 0
        self.Gs = []
        while sum([sum(self.test_on_pattern(pattern, target)) for pattern, target in zip(patterns, targets)])\
        != len(targets) * len(targets[0]) and epoch < 500:
            # print("epoch:", epoch)
            # print("weights:", self.get_weights())
            # for p in patterns:
            #     print(self.forward(p))
            epoch += 1
            for pattern, target in zip(patterns, targets):
                self.forward(pattern)
                self.backward(target)
                self.update_weight_changes(self.learning_rate)
                # print("sample weight change:", list(self.connections_forward[-1].values())[-1].get_weight_change())
            self.update_weights(self.momentum) # this will initialize weight_changes
            self.Gs.append(self.get_G(patterns, targets))
        if hard:
            while epoch < 500:
                epoch += 1
                for pattern, target in zip(patterns, targets):
                    self.forward(pattern)
                    self.backward(target)
                    self.update_weight_changes(self.learning_rate)
                self.update_weights(self.momentum) # this will initialize weight_changes
                self.Gs.append(self.get_G(patterns, targets))

        # print("final weights:", self.get_weights())
        return epoch

    # get global error on a set of patterns
    def get_G(self, patterns: Sequence, targets: Sequence) -> float:
        return sum([sum(self.test_on_pattern(pattern, target, True)) / len(target) for pattern, target in zip(patterns, targets)]) / len(targets)
    
    def set_learning_rate(self, learning_rate):
        self.learning_rate = learning_rate

    def set_momentum(self, momentum):
        self.momentum = momentum
    
    def get_output(self) -> list:
        return [unit.get_activation() for unit in self.units[-1]]
    
    def get_weights(self) -> list:
        return [[c.get_weight() for c in layer.values()] for layer in self.connections_forward]
    
    def get_training_patterns(self) -> list:
        return self.training_patterns

    def init(self):
        for conns in self.connections_forward.values():
            for c in conns:
                c.init()
        self.training_patterns = []
        self.Gs = []


