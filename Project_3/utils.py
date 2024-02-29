import random
from typing import Sequence
from HopfieldNet import HopfieldNet

def get_flip_pattern(pattern: Sequence, prob: float):
    # assuming input pattern is a sequence of 0 and 1
    # returning a different object than the input one
    ret = []
    for i in range(len(pattern)):
        if random.random() > prob:
            ret.append(pattern[i])
            continue
        if pattern[i] == 0:
            ret.append(1)
        else:
            ret.append(0)
    return ret

def get_random_pattern(num: int = 16, prob: float = 0.5):
    ret = []
    for _ in range(num):
        if random.random() > 0.5:
            ret.append(1)
        else:
            ret.append(0)
    return ret

def run_tests(network : HopfieldNet, orig_patterns: list, *args: Sequence, sync: int=1, get_states = False):
    # tests format: probs * ptts * runs (5) * 16
    tests = [*args]
    times = []
    hamming_disances = []
    energies = []
    if get_states:
        states = []
    for prob in range(len(tests)):
        times_l1 = []
        hamming_l1 = []
        energies_l1 = []
        if get_states:
            states_l1 = []
        for init_ptt in range(len(tests[0])):
            times_l2 = []
            hamming_l2 = []
            energies_l2 = []
            if get_states:
                states_l2 = []
            for run in range(5):
                time, hamming, energy = network.run_to_settle(orig_patterns[init_ptt], tests[prob][init_ptt][run], sync)
                times_l2.append(time)
                hamming_l2.append(hamming)
                energies_l2.append(energy)
                if get_states:
                    states_l2.append(network.get_pattern())
            times_l1.append(times_l2)
            hamming_l1.append(hamming_l2)
            energies_l1.append(energies_l2)
            if get_states:
                states_l1.append(states_l2)
        times.append(times_l1)
        hamming_disances.append(hamming_l1)
        energies.append(energies_l1)
        if get_states:
            states.append(states_l1)
    if get_states:
        return times, hamming_disances, energies, states
    else: 
        return times, hamming_disances, energies

def get_mean(s: Sequence):
    # input format: 
    means = []
    for i in s:
        mean_l1 = []
        for j in i:
            if not None in j:
                mean_l1.append(sum(j) / len(j))
            else: 
                mean_l1.append(None)
        means.append(mean_l1)
    return means