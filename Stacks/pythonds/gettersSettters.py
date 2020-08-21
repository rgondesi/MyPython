class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity
    
    @property
    def number_of_wheels(self):
        return self.__number_of_wheels
    
    @number_of_wheels.setter
    def number_of_wheels(self, number):
        self.__number_of_wheels = number

v = Vehicle(4,"v6",5, 200)


print(v.number_of_wheels)
#print(v.number_of_wheels(6))
v.number_of_wheels = 6
print(v.number_of_wheels)