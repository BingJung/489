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

    def set_pattern(self, pattern: Sequence):
        pattern_l = len(pattern)
        assert pattern_l == self.size, \
        f"length of input pattern should be {self.size} rather than {pattern_l}."
        for i in range(pattern_l):
            self.units[i].set_activation(pattern[i])
    
    def train_on_pattern(self, pattern: Sequence):
        self.set_pattern(pattern)
        for conn in self.conns_dict.values():
            if conn.same_activations():
                conn.add_weight(1)
            else:
                conn.add_weight(-1)

    def run_to_settle(self, pattern: Sequence = None) -> tuple[int, int, list]: # reutrning times of iteration to settling
        if pattern != None:
            self.set_pattern(pattern)
        settled = False
        times = 0
        energies = []
        while not settled:
            indices = [i for i in range(self.size)]
            random.shuffle(indices)
            # print("indices:", indices)
            settled = True
            for i in indices:
                # print("index:", i)
                self.update_all_inputs()
                times += 1
                energies.append(self.get_energy())
                if self.units[i].update_activation():
                    # print("updated")
                    settled = False
                    break
            if times > 10000:
                return times
        self.update_all_inputs()
        hamming_dis = [i!=j for i, j in zip(self.get_pattern(), pattern)].count(True)
        return (times - 15, hamming_dis, energies[:-15])

    def get_energy(self):
        energy = 0
        for conn in self.conns_dict.values():
            energy -= 0.5 * conn.get_weight() * int(conn.same_activations())
        return energy

    def get_pattern(self) -> list:
        return [unit.activation for unit in self.units]
            
    def update_all_inputs(self):
        for unit in self.units:
            unit.get_input()

    def init_weights(self):
        for conn in self.conns_dict.values:
            conn.init_weight()

    
