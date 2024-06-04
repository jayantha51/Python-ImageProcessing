# duck typing: concept where the class of an object is less important  than the methods
# class typ is not minimum methods/attributes are present
# "if it walks like a duck, and it quack like a duck, then it must be a duck"

class Duck:
    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quacking")


class Chicken:
    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("this chicken is clucking")


class Person():
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("you caught the critter")


def main():
    duck = Duck()
    chicken = Chicken()
    person = Person()
    person.catch(chicken)


if __name__ == '__main__':
    main()
