def main():
    def double(x):
        return x * 2

    print(double(3))

    triple = lambda x: x * 3
    print(triple(4))

    multiple = lambda a, b: a * b
    print(multiple(5, 7))

    full_name = lambda first_name, last_name: first_name + " " + last_name

    print("Full name is ", full_name("Jayantha", "Senawiratne"))

    age_check = lambda age: True if age >= 18 else False
    print("Are you an adult True/False: ", age_check(19))
    print((lambda p, q: p * q)(6, 7))

    higher_order_function1 = lambda z, function1: z + function1(z)
    print("The solution for the first higher order function is: ", higher_order_function1(3, lambda z: z * z))

    higher_order_function2 = lambda a, b, c, function2: function2(a, b) + c
    print("Solution for the second higher order function is: ",
          higher_order_function2(2, 3, 4, function2=lambda a, b: a * b))


if __name__ == '__main__':
    main()
