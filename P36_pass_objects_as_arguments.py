class Car:
    color = None


class Bike:
    color = None


def change_color(Vehicle, color):
    Vehicle.color = color


def main():
    car1 = Car()
    car2 = Car()
    bike1 = Bike()

    change_color(car1, "black")
    change_color(car2, "red")
    change_color(bike1, "blue")

    print(car1.color)
    print(car2.color)
    print(bike1.color)


if __name__ == '__main__':
    main()
