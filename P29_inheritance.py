class Animal:
    alive  = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming")

class Eagle(Animal):
    def fly(self):
        print("This eagle is flying")

def main():
    rabbit1 =Rabbit()
    fish1 = Fish()
    eagle1 = Eagle()

    rabbit1.alive
    rabbit1.eat()
    rabbit1.sleep()
    rabbit1.run()

    fish1.swim()
    eagle1.fly()
if __name__ == '__main__':
    main()


