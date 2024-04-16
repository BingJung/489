from typing import Sequence
from BPNet import BPNet

class Embedder:
    def __init__(self, dictionary: Sequence = None, structure: Sequence = None, learning_rate: float = None, momentum: float = None) -> None:
        for i in structure:
            assert type(i) == int, "structure has to be a sequence of integers"
        self.structure = [i for i in structure]

        self.dict = {key : ind for ind, key in enumerate(dictionary)}
        self.dict_size = len(dictionary)
        if self.dict != {}:
            # start fitting
            self.net = BPNet((len(self.dict), *structure), learning_rate=learning_rate, momentum=momentum)

    def fit_on_dict(self, dictionary):
        if self.dict != {}:
            print(f"The original dictionary with size {len(self.dict)} will be forgotten. The orginal net will also be refreshed.")
        self.dict = {key : ind for ind, key in enumerate(dictionary)}
        if self.structure != []:
            print(f"The network is initialized respecting to dictionary with size {len(dictionary)}.")
            self.net = BPNet((len(self.dict), *self.structure), learning_rate=self.net.learning_rate, momentum=self.net.momentum)

    def alter_params(self, structure: Sequence = None, learning_rate: float = None, momentum: float = None):
        if learning_rate != None:
            self.net.learning_rate = learning_rate
        if momentum != None:
            self.net.momentum = momentum
        if structure != None:
            self.structure = structure
            if self.dict != {}:
                print(f"The network is initialized with structure {structure}.")
                self.net = BPNet((len(self.dict), *self.structure), learning_rate=self.net.learning_rate, momentum=self.net.momentum)

    def embed(self, word):
        assert word in self.dict, f'Input "{word}" not found in the dictionary.'
        one_hot = [0 for _ in range(self.dict_size)]
        one_hot[self.dict[word]] = 1
        return self.net.forward(pattern=one_hot)