def main():
    print("function is a block of code which is executed only when it is called")

    def hi():
        pass

    def hello():
        print("printing hello")

    hello()  # calling this will print statement under hello

    def hello_name(name):
        print("Hello", name)

    hello_name("Sayumee")

    def hello_full_name(first_name, last_name):
        print("Hello", first_name, last_name)

    hello_full_name("Jayantha", "Senawiratne")

    def hello_name_age(first_name, last_name, age):
        print(first_name, last_name, str(age))

    hello_name_age("Sayumee", "Senawiratne", 15)


if __name__ == '__main__':
    main()
