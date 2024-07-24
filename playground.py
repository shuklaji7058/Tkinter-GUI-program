def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 4, 5, 8, 9, 2))

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]

calculate(2, add=5, multiply=8)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Jaguar", model="F-Pace")
print(my_car.model)
