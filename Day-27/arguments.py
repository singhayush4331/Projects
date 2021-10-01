# *args --> Positional Arguements.

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


# print(add(2, 4, 6, 7, 1))

# **kwargs --> Keyword Arguements.

def calculate(n, **kwargs):
    print(kwargs)
    for key, values in kwargs.items():
        print(key)
        print(values)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


# .items() --> Used to return the list with all dictionary key values.
# Datatype of args --> Tuple
# Datatype of kwargs --> Dictionary


# calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seat = kwargs.get("seat")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
print(my_car.model)

