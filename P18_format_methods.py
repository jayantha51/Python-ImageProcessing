print("str.format() =  optional methods that gives users"
      "more control when displaying output")


def main():
    animal = "cow"
    item = "moon"

    print("First: The " + animal + " jump over the " + item)
    print("Second:  The {} jumped over the {}".format(animal, item))
    print("Third: The {} jumped over the {}".format("cow", "moon"))
    print("Fourth: The {} jumper over the {}".format(item, animal))  # positional agument
    print("Fifth: The {a} jumped over the {b}".format(a="cow", b="moon"))

    # next level
    text = "Sixth: The {} jumped over the {}"
    print(text.format(animal, item))

    print("_____________________________")
    name = "Charm"
    print("Hello my name is {}".format(name))
    print("hello my name is {:10} how is your day".format(name))
    print("hello my name is {:<10} how is your day".format(name))
    print("hello my name is {:>10} how is your day".format(name))
    print("hello my name is {:^10} how is your day".format(name))

    print("_____________________________")
    pi = 3.14159
    n = 100000

    print("value of Pi is {:0.2f}".format(pi))
    print("value of the number is {:,}".format(n))
    print("binary representation of the number is {:b}".format(n))
    print("engineering representation of the number is {:E}".format(n))


if __name__ == '__main__':
    main()
