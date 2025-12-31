#Coding a flight management program

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

persons = ["Eric", "Enock", "John", "Peter"]

for person in persons:
    success = flight.add_passenger(person)
    if success:
        print(f"We have successfully added {person} to the flight!")
    else:
        print(f"We have unfortunately no seat left for {person}!")