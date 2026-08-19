
#La herencia multiple nos deja que una clase herede de dos o más clases al mismo tiempo. 
#Podemos hacerlo pasando una lista de clases padre separadas por comas.

class Vehicle:

    def start(self):
        print("El vehículo está encendido")

    def stop(self):
        print("El vehículo está apagado")


class Flying:

    def fly(self):
        print("El vehículo está volando")


class FlyingCar(Vehicle, Flying):

    def drive(self):
        print("El auto está funcionando")