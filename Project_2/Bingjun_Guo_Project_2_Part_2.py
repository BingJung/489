class AcFuncOne():
    def __init__(self, gamma=0) -> None:
        self.activation = 0
        self.gamma = gamma

    def set_gamma(self, gamma):
        self.gamma = gamma

    def initialize(self):
        self.activation = 0

    def activate(self, input):
        change = self.gamma * (1 - self.activation) * input
        self.activation += change
        return self.activation
    
class AcFuncTwo():
    def __init__(self, gamma=0, delta=0) -> None:
        self.activation = 0
        self.gamma = gamma
        self.delta = delta

    def set_gamma(self, gamma):
        self.gamma = gamma
    
    def set_delta(self, delta):
        self.gamma = delta

    def initialize(self):
        self.activation = 0

    def activate(self, input):
        change = self.gamma * (1 - self.activation) * input - self.delta * self.activation
        self.activation += change
        return self.activation
    
class AcFuncThree():
    def __init__(self, gamma=0, delta=0) -> None:
        self.activation = 0
        self.gamma = gamma
        self.delta = delta

    def set_gamma(self, gamma):
        self.gamma = gamma
    
    def set_delta(self, delta):
        self.gamma = delta

    def initialize(self):
        self.activation = 0

    def activate(self, e, i):
        change = self.gamma * ((1-self.activation)*e + (1+self.activation)*i) - self.delta * self.activation
        self.activation += change
        return self.activation
    
# main
rule_a = AcFuncOne(0.5)
rule_a.initialize()
for i in range(10):
    rule_a.activate(1.5)
print("result for a1:", rule_a.activation)

rule_a.initialize()
for i in range(10):
    rule_a.activate(5.0)
print("result for a2:", rule_a.activation)

rule_a.initialize()
for i in range(10):
    rule_a.activate(3.0)
print("result for a3:", rule_a.activation)

rule_a.initialize()
for i in range(2):
    rule_a.activate(1)
for i in range(5):
    rule_a.activate(-1)
print("result for a4:", rule_a.activation)

rule_a.initialize()
for i in range(10):
    rule_a.activate(1)
for i in range(5):
    rule_a.activate(-1)
print("result for a5:", rule_a.activation)

rule_b = AcFuncTwo(0.5, 0.1)
rule_b.initialize()
for i in range(10):
    rule_b.activate(1)
for i in range(5):
    rule_b.activate(-1)
print("result for b1:", rule_b.activation)

rule_c = AcFuncThree(0.5, 0.1)
rule_c.initialize()
for i in range(10):
    rule_c.activate(1, 0)
for i in range(5):
    rule_c.activate(0, -1)
print("result for c1:", rule_c.activation)