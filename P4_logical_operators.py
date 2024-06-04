def main():
    # first case:

    your_age = int(input("enter your age: "))
    if (your_age <= 0 or your_age >= 121):
        print("invalid entry")
    elif (your_age < 18):
        print("you are child")
    elif (your_age == 100):
        print("you are 100 years old!!!")
    elif (your_age < 65):
        print("you are an adult")
    else:
        print("you are a senior")

    # Second
    temperature = int(input("Enter the temperature: "))
    if not (temperature >= 65 and temperature <= 80):
        print("stay indoors")
    elif (temperature >= 65 and temperature <= 80):
        print("it is a beautiful day enjoy")

    # third case:
    first_name = ""
    while len(first_name) == 0:
        first_name = input("Enter your first name: ")
    last_name = None
    while not (last_name):
        last_name = input("Enter your last name: ")

    print("Hello",first_name.capitalize(), last_name.capitalize(), "how are you this morning")

if __name__ == '__main__':
    main()