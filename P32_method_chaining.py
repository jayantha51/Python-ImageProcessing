# method chaining = calling multiple methods sequentially
# each call performs an action on the same object
# and returns self

class Car:
    def turn_on(self):
        print("This car starts")
        return(self)

    def drive(self):
        print("This car drives well")
        return(self)

    def brake(self):
        print("This care stops immediately after breaks")
        return (self)
    def turn_off(self):
        print("This car turns off")
        return (self)

def main():
    car =Car()

    car.turn_on().drive().brake().turn_off()

    print("next.......................")
    car.turn_on().\
        drive().\
        brake().\
        turn_off()
if __name__ == '__main__':
    main()

