class Prey:
    def flee(self):
        print("This animal flees")


class Predator:
    def hunt(self):
        print("This animal hunts")


class Rabbit(Prey):
    pass


class Eagle(Predator):
    pass


class Fish(Prey, Predator):
    pass


def main():
    rabbit = Rabbit()
    eagle = Eagle()
    fish = Fish()

    rabbit.flee()
    eagle.hunt()
    fish.flee()
    fish.hunt()


if __name__ == '__main__':
    main()
