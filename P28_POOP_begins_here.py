from car import Car

def main():
    car1 = Car("BMW", "328i","2015","white")
    car2 = Car("NISSAN", "Altima", 2014, "black")

    print("Type1: make: ", car1.make, " model: ", car1.year, " color: ", car1.color)
    print("Type1: make: ", car2.make, " model: ", car2.year, " color: ", car2.color)
    print("____________________________________")

    car1.drive()
    car1.stop()

    print("Number of wheels in type 1 is: ", str(car1.wheels))
    Car.wheels = 6
    print("number of wheels in Type 2 car is ", str(car2.wheels))

    Car.wheels = 8
    print(car1.wheels)
    print(car2.wheels)

if __name__ == '__main__':
    main()