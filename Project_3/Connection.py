from Unit import Unit

class Connection:
    # allowing unknown input units for construction
    def __init__(self, recipient: Unit = None, sender: Unit = None, weight = 0.0):
        self.recipient = recipient
        self.sender = sender
        self.weight = weight

    def set_recipient(self, unit):
        self.recipient = unit

    def set_sender(self, unit):
        self.sender = unit

    def set_weight(self, weight):
        self.weight = weight
    
    def add_weight(self, d):
        self.weight += d

    def init_weight(self):
        self.weight = 0

    def get_weight(self):
        return self.weight
    
    def same_activations(self) -> bool:
        return self.recipient.get_activation() == self.sender.get_activation()