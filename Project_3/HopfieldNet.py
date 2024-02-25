from typing import Sequence, Dict
from Connection import Connection
from Unit import Unit

class HopfieldNet:
    def __init__(self, units: Sequence[Unit], conns: Dict[str, Connection]) -> None:
        # assuming all units are connecting each other without checking here
        # assuming connections: conns["(i, j)": Connection]
        self.units = units
        self.conns_dict = conns
        self.size = len(units)

    def train_on_pattern(self, pattern: Sequence):
        pattern_l = len(pattern)
        assert pattern_l == self.size, \
        f"length of input pattern should be {self.size} rather than {pattern_l}."
        for i in range(self.size):
            self.units[i].set_activation(pattern[i])
        for conn in self.conns_dict.values():
            if conn.same_activations():
                conn.add_weight(1)
            else:
                conn.add_weight(-1)

    def init_weights(self):
        for conn in self.conns_dict.values:
            conn.init_weight()