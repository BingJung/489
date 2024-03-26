from Unit import Unit

class Connection:
    # allowing unknown input units for construction
    def __init__(self, sender: Unit = None, recipient: Unit = None, weight = 0.5):
        self.sender = sender
        self.recipient = recipient
        self.weight = weight
        self.weight_change = 0

    def set_recipient(self, unit):
        self.recipient = unit

    def set_sender(self, unit):
        self.sender = unit

    def set_weight(self, weight):
        self.weight = weight
    
    # returning the current weight change (not including momentum)
    def update_weight(self, learning_rate=  0.5, momentum = 0) -> float:
        self.weight += self.weight_change * momentum
        self.weight_change = learning_rate * self.recipient.error * self.sender.activation
        self.weight += self.weight_change
        return self.weight_change


    def init_weight(self):
        self.weight = 0

    def get_weight(self) -> float:
        return self.weight
    
    def same_activations(self) -> bool:
        return self.recipient.get_activation() == self.sender.get_activation()