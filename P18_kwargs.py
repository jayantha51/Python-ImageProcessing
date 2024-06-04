print("parameter that will pack all arguments into a dictionary"
      "useful so that a function can accept a varying amount of keyword argument")


def main():
    def function_namel(first_name, last_name):
        print("Hi", first_name, last_name)

    function_namel("Jayantha", "Senawiratne")

    def function_name2(**kwargs):
        print("Hi" + " " + kwargs["first_name"] + " " + kwargs["last_name"])

    function_name2(first_name="Jayantha", middle_name="test",
                   last_name="Senawiratne")  # this will not print middel name

    def function_name3(**kwargs):
        for key, value in kwargs.items():
            print(value, end=" ")
    function_name3(calling = "Hi", title = "Ms.", first_name = "Sayumee", Midle_initial = "H", last_name = "Senawiratne")

if __name__ == '__main__':
    main()
