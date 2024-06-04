class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")

def main():
    rabbit = Rabbit()
    print("Is rabbit alive True or False:", rabbit.alive)
    rabbit.eat()
    rabbit.run()
if __name__ == '__main__':
    main()