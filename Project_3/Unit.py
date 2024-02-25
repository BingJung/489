class Unit:
    def __init__(self, threshold = 0) -> None:
        self.input = 0.0
        self.activation = 0.0
        self.threshold = threshold
        self.incoming_connections = []
        self.outgoing_connections = []

    # question: how to enable class constraint here and avoid circular import
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
        if self.input > self.threshold:
            self.activation = 1
        else:
            self.activation = 0
        return self.activation
    
    def init_io(self):
        self.input = 0
        self.activation = 0

    def set_activation(self, activation):
        self.activation = activation

    def get_activation(self):
        return self.activation