def main():
    first_name  = input("Enter your first name: ")
    last_name = input("Enter you last name: ")
    age = int(input("How old are you: "))
    full_name = lambda first_name, last_name: first_name + " " + last_name
    print("Hello", full_name(first_name,last_name))
    # solve following equation 2x + 3*y + 4z
    print("Here is the solution: ",(lambda x, y, z: 2 * x + 3 * y + 4 * z) (3,4,5))


if __name__ == '__main__':
    main()