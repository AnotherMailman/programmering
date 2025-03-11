import random

class Passenger:
    def __init__(self, name : str, destination : int):
        self.name = name
        self.destination = destination
    

class Wagon:
    def __init__(self, passenger : list):
        self.passenger = passenger

class Train:
    def __init__(self, wagons : list, line : int, position : int):
        self.wagons = wagons
        self.line = line
        self.position = position

class Station:
    def __init__(self, name : str, passenger : list[Passenger]):
        self.name = name
        self.passenger = passenger

class Line:
    def __init__(self, name : str, stops : list):
        self.name = name
        self.stops = stops

first = [
    "James ", "Michael ", "Robert ", "john ", "David ", "William ", "Richard ", "Joseph ", "Thomas ", "Christopher ", "Charles ", "Daniel ", "Matthew ", "Peter ", "Jane "
]

last = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Griffin", "Gonzales", "Wilson", "Doe"
]

stations = [
    Station("Åre", []),
    Station("Östersund", []), 
    Station("Sundsval", []),
    Station("Umeå", []),
    Station("Gävle", [])
]

lines = [
    Line("Blåa Linjen", [0, 1, 2, 3])
]

trains = [
    Train([Wagon([]), Wagon([]), Wagon([])], 0, 0)
]


for i in range(10):
    random.shuffle(first)
    random.shuffle(last)
    random_position = random.randrange(0, len(stations))
    passenger = Passenger(first[0] + last[0], stations[random_position])
    stations[random_position].passenger.append(passenger)
    first.pop(0)
    last.pop(0)

for x in stations:
    print(x.passenger)

#############
# Game Loop #
#############
while True:

    # Kolla om passagerare vill hoppa på tåg
    for train in trains:
        if (Wagon[passanger.destination]) in train.position:
            train.wagons.append(passanger)
            station
        else:
            pass



    # Kolla om passaerare vill hoppa av tåg

    # Flytta alla tåg

    for train in trains:
        if train.line < (len(Line[0])):
            train.line += 1
        else:
            train.line = 0