print("a changeable, unordered collection of unique key: values pairs "
      "fast because they use hashing, allows us to access a value quickly")


def main():
    capitals = {"Sri Lanka": "Kandy",
                "England": "London",
                "Japan": "Tokyo"}

    print("Capital of Sri Lanka is:", capitals["Sri Lanka"])
    print(capitals.keys())
    print(capitals.values())
    print(capitals.items())

    capitals.update({"France": "Paris"})
    print(capitals.items())
    capitals.update({"Sri Lanka": "Colombo"})
    print(capitals.items())

    for key, value in capitals.items():
        print(key, value)

    print("let's check clear")
    capitals.clear()
    for key, value in capitals.items():
        print(key, value)


if __name__ == '__main__':
    main()
