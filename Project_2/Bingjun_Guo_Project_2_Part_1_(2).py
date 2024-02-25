class Connection:
    # allowing unknown input units for construction
    def __init__(self, recipient = None, sender = None, weight = 0.0):
        self.recipient = recipient
        self.sender = sender
        self.weight = weight

    def set_recipient(self, unit):
        self.recipient = unit

    def set_sender(self, unit):
        self.sender = unit

class Unit:
    def __init__(self) -> None:
        self.input = 0.0
        self.activation = 0.0
        self.incoming_connections = []
        self.outgoing_connections = []

    def add_connection(self, connection):
        assert connection.recipient == self or connection.sender == self, \
        "target unit is not involved in the input connection."
        assert connection.recipient != None and connection.sender != None, \
        "the connection is not complete."
        # allowing for self-self connection
        if connection.recipient == self:
            self.incoming_connections.append(connection)
        if connection.sender == self:
            self.outgoing_connections.append(connection)
        
    def get_input(self):
        self.input = sum(i.sender.activation * i.weight for i in self.incoming_connections)
        return self.input

    def update_activation(self):
        if self.input > 1:
            self.activation = 1
        elif self.input < 0.75:
            self.activation = 0
        else: self.activation = self.input
        return self.activation
    
    def initialize(self):
        self.input = 0
        self.activation = 0

    def set_activation(self, activation):
        self.activation = activation
    
# main
################Part 1 (1)################
# building nodes
a = Unit()
b = Unit()
c = Unit()
# building connections
conn_ab = Connection(a, b, 1.0)
conn_ba = Connection(b, a, 1.0)
conn_ac = Connection(a, c, 1.0)
conn_ca = Connection(c, a, 1.0)
conn_bc = Connection(b, c, 1.0)
conn_cb = Connection(c, b, 1.0)
# adding connections
a.add_connection(conn_ab)
a.add_connection(conn_ba)
a.add_connection(conn_ac)
a.add_connection(conn_ca)
b.add_connection(conn_ba)
b.add_connection(conn_ab)
b.add_connection(conn_bc)
b.add_connection(conn_cb)
c.add_connection(conn_cb)
c.add_connection(conn_bc)
c.add_connection(conn_ca)
c.add_connection(conn_ac)
# experiments
a.set_activation(1.0)
b.set_activation(1.0)
print("first experiment begin; activations:", a.activation, b.activation, c.activation)
for i in range(10):
    a.get_input()
    b.get_input()
    c.get_input()
    a.update_activation()
    b.update_activation()
    c.update_activation()
print("results:", a.activation, b.activation, c.activation)

a.initialize()
b.initialize()
c.initialize()
a.set_activation(1.0)
print("second experiment begin; activations:", a.activation, b.activation, c.activation)
for i in range(10):
    a.get_input()
    b.get_input()
    c.get_input()
    a.update_activation()
    b.update_activation()
    c.update_activation()
print("results:", a.activation, b.activation, c.activation)

a.initialize()
b.initialize()
c.initialize()
a.set_activation(0.5)
print("third experiment begin; activations:", a.activation, b.activation, c.activation)
for i in range(10):
    a.get_input()
    b.get_input()
    c.get_input()
    a.update_activation()
    b.update_activation()
    c.update_activation()
print("results:", a.activation, b.activation, c.activation)


