from typing import Sequence, Dict
from Connection import Connection
from Unit import Unit

import random

class HopfieldNet:
    def __init__(self, units: Sequence[Unit], conns: Dict[str, Connection]) -> None:
        # assuming all units are connecting each other without checking here
        # assuming connections: conns["(i, j)": Connection]
        self.units = units
        self.conns_dict = conns
        self.size = len(units)
        self.training_patterns = []

    def set_pattern(self, pattern: Sequence):
        pattern_l = len(pattern)
        assert pattern_l == self.size, \
        f"length of input pattern should be {self.size} rather than {pattern_l}."
        for i in range(pattern_l):
            self.units[i].set_activation(pattern[i])
        self.training_patterns.append(pattern)
    
    def train_on_pattern(self, pattern: Sequence):
        self.set_pattern(pattern)
        for conn in self.conns_dict.values():
            if conn.same_activations():
                conn.add_weight(1)
            else:
                conn.add_weight(-1)
        self.training_patterns.append(pattern)
    
    def run_to_settle(self, orig_pattern: Sequence, pattern: Sequence=None, n_per_it: int=1) -> tuple[int, int, list]:
        if pattern != None:
            self.set_pattern(pattern)
            self.update_all_inputs() 
        settled = False
        times = 0
        energies = []
        while not settled: # an iteration begins
            n = n_per_it
            indices = [i for i in range(self.size)]
            random.shuffle(indices)
            # print("indices:", indices)
            settled = True
            for i in indices: # this loop ends when n nodes are successfully updated
                # print("index:", i)
                times += 1
                energies.append(self.get_energy())
                if self.units[i].update_activation():
                    # print("updated")
                    settled = False
                    n -= 1
                if n==0:
                    break
            self.update_all_inputs()
            if times > 1234:
                return (None, None, energies)
        self.update_all_inputs()
        hamming_dis = [i!=j for i, j in zip(self.get_pattern(), orig_pattern)].count(True)
        return (times-1, hamming_dis, energies[:-15]) 

    def get_energy(self):
        energy = 0
        for conn in self.conns_dict.values():
            energy -= 0.5 * conn.get_weight() * int(conn.same_activations())
        return energy

    def get_pattern(self) -> list:
        return [unit.activation for unit in self.units]
    
    def get_training_patterns(self) -> list:
        return self.training_patterns
            
    def update_all_inputs(self):
        for unit in self.units:
            unit.get_input()

    def init_weights(self):
        for conn in self.conns_dict.values:
            conn.init_weight()
        self.training_patterns = []


    
