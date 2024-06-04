print("The origin of a variable is recognized"
      "a variable is only available from inside the origin it is created."
      "A globally and locally scoped versions of a variables can be created")


def main():
    name = "global name is Pi"

    def display_name():
        name = "local name is Charm"

    print(name)

    print(name)


if __name__ == '__main__':
    main()
