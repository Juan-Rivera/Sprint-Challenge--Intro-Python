# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    pass

# base class: Flight Vehicle
class FlightVehicle(Vehicle):
    pass

# base class: Starship
class Starship(FlightVehicle):
    pass

# base class: Airplane
class Airplane(FlightVehicle):
    pass

# base class: Ground Vehicle
class GroundVehicle(Vehicle):
    pass

# base class: Car
class Car(GroundVehicle):
    pass

# base class: Motorcycle
class Motorcycle(GroundVehicle):
    pass
