print("argument proceed by an identifiers when we pass them to a function"
      "The order of the argument does not matter, unlike position argument"
      "Python knows the name of the argument that our function was receives")


def main():
    # Here us an example of positional argument in which position does matter
    def hello1(first_name, middle_name, last_name):
        print("Hello ", first_name, middle_name, last_name)

    hello1("Ashwin", "H", "Senawiratne")

    # Here is an example om which keyword argument works
    def hello2(firs_name, middle_name, last_name):
        print("Hello", firs_name, middle_name, last_name)

    hello2(last_name="Senawiratne", firs_name="Ashwin", middle_name="H")


if __name__ == '__main__':
    main()
