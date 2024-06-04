# walrus operator :=
# new to python 3.8
# assign expression aka walrus operator
# assign values to variables as part of larger expression

def main():
    # first method
    happy = True
    print(happy)

    # second method
    print(second_happy_happy_true := True)

    # The first method
    foods = list()

    while True:
        food = input("what type of fodd do you want? ")
        if food == "quit":
            break
        foods.append(food)

    # The second method

    foods = list()
    while food := input("what food do you like?: ") != "quit":
        foods.append(food)

if __name__ == '__main__':
    main()