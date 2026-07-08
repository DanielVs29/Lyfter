class Person:
    def __init__(self, name):
        self.name = name


class Bus:
    def __init__(self, max_passengers=4):
        self.max_passengers = max_passengers
        self.count = 0
        self.passengers = []


    def add_passenger(self, person):
        if self.count >= self.max_passengers:
            print("The bus is full.")
        else:
            self.passengers.append(person)
            self.count += 1
            print(f"Passenger: {person.name} added to the bus!")


    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            self.count -= 1
            print(f"{person.name} got off the bus.")
        else:
            print(f"{person.name} is not on the bus.")


person1 = Person("Daniel")
person2 = Person("Maria")
person3 = Person("Juan")
person4 = Person("Marta")
person5 = Person("Pedro")

the_bus = Bus()

the_bus.add_passenger(person1)
the_bus.add_passenger(person2)
the_bus.add_passenger(person3)
the_bus.add_passenger(person4)
the_bus.add_passenger(person5)

the_bus.remove_passenger(person1)
the_bus.remove_passenger(person2)
the_bus.remove_passenger(person3)
the_bus.remove_passenger(person4)
the_bus.remove_passenger(person5)