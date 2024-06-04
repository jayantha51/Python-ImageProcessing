# prevent user from creating object of that class
# + compels  a user to override abstract methods in a child class
# abstract class = a class which contains one of more abstract methods
# abstract method = a method that has a declaration but does not have an implementation

from abc import abstractmethod, ABC

class Vehicle(ABC):

    def go(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError

class Bus(Vehicle):
    def go(self):
        print("This bus drives well")
    def stop(self):
        print("This bus stops")

class Van(Vehicle):
    def go(self):
        print("this van drives well")

    def stop(self):
        print("this van stops")

def main():
    bus = Bus()
    van = Van()

    bus.go()
    bus.stop()
    print("next ______________________")
    van.go()
    van.stop()
if __name__ == '__main__':
    main()