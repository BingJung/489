import random

### functions
# roll_dices
# input: either in form "dices = n, sides = m" or enter numbers of sides of each dice seperated by comma
# output: ([results], sum)
# note: numbers of sides should be greater than 0; dices are fair; ignoring being Platonic solids or not
def roll_dices (*args, **kwargs):
    assert args == () or kwargs == {}, \
    "please either input number of sides of dices one by one or \
    assert that each dice has the same number of sides and only \
    enter two arguments."
    sides_list = []
    if args == ():
        assert list(kwargs.keys()) == ['dices', 'sides'] and args == (), "All dices share the same number of sides;\
            should enter two arguments in order: dices = n, sides = m"
        for i in range(kwargs['dices']):
            assert kwargs['sides'] >= 0, "number of sides needs to be greater than zero."
            sides_list.append(kwargs['sides'])
    else:
        for num in args:
            assert num > 0, "number of sides needs to be greater than zero."
            sides_list.append(num)

    output_list = []
    for num in sides_list:
        output_list.append(random.randint(1, num))
    return (output_list, sum(output_list))
    
# count_odds
# input: an integer list
# output: number of odd numbers in the input
def count_odds (input_list):
    assert type(input_list) == list, "please enter a integer list as input."
    num = 0
    for i in input_list:
        assert type(i) == int, "cannot judge non-integers."
        if i % 2 != 0:
            num += 1
    return num

### test cases
print("Tests for the first function:")
result, s = roll_dices(dices = 20, sides = 5)
print("input: dices = 20, sides = 5")
print("result:", result)
print("sum:", s)
result, s = roll_dices(1, 2, 3, 4, 5)
print("input: (sides =) 1, 2, 3, 4, 5")
print("result:", result)
print("sum:", s)
result, s = roll_dices(66, 8748, 3, 5, 79, 32, 5432, 54, 43, 3)
print("input: (sides =) 66, 8748, 3, 5, 79, 32, 5432, 54, 43, 3")
print("result:", result)
print("sum:", s, "\n")

print("Tests for the second function:")
num = count_odds([1, 3, 5, 7, 9])
print("input: [1, 3, 5, 7, 9]")
print("number of odd numbers:", num)
num = count_odds([0, 0, 0, 0, 0])
print("input: [0, 0, 0, 0, 0]")
print("number of odd numbers:", num)
num = count_odds([-1, -3, -4, -6, 7, 9, 0])
print("input: [-1, -3, -4, -6, 7, 9, 0]")
print("number of odd numbers:", num, "\n")

### classes
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
    def __init__(self, threshold = 0.5) -> None:
        self.threshold = threshold
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
        if self.input >= self.threshold:
            self.activation = 1.0
        else:
            self.activation = 0.0
        return self.activation

# tests
haha = Unit()
hoho = Unit()
haha.activation = 1.0
hiehie = Unit()
conn1 = Connection(hiehie, weight = 0.8)
conn2 = Connection(hiehie, hoho)
conn1.set_sender(haha)
hiehie.add_connection(conn1)
hiehie.add_connection(conn2)
print("hiehie's incoming connection list:", hiehie.incoming_connections)
print("hiehie's input:", hiehie.get_input())
print("hiehie's activation with threshold as 0.5:", hiehie.update_activation())
        
