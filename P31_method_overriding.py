class Animal:
    def eat(self):
        print("This animal eats")


class Rabbits(Animal):

    def eat(self):
        print("This fish eats")


def main():
    animal = Animal()
    rabbit = Rabbits()
    animal.eat()
    rabbit.eat()


if __name__ == '__main__':
    main()
