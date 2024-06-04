print("break: uses to terminate the loop entirely")
print("continue: to skips to the next iteration of the loop")
print("pass: does nothing, acts as a p[lace holder\n")


def main():
    # break

    while True:
        name = input("Enter your name: ")
        if name != "":
            break

    # continue
    phone_number = "669-946-2378"

    for i in phone_number:
        if i == "-":
            continue
        print(i, end="")

    print("\n")
    # pass

    for letter in "python":
        if letter == "h":
            pass
            print("this is pass block")
        print("this is curent letter", letter)
    print("for loop ends here")


if __name__ == '__main__':
    main()
