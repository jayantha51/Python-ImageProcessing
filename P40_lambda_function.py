# function written in a 1 line using labda keyword
# accepts any number of arguments, but only has one expression.
#  (think of it as a shortcut useful it needed for a short period of time then dumped it)
# Syntax = lambda parameter: expression

def main():
    def double(x):
        return x * 2

    print(double(7))

    # the same thing can be done using lambda function
    triple = lambda y: y * 3
    print(triple(121))

    multiply = lambda a, b: a * b
    print(multiply(3, 39))

    full_name = lambda first_name, last_name: first_name + " " + last_name
    print(full_name("Jayantha", "Senawiratne"))

    age_check = lambda age: True if age >= 18 else False
    print(age_check(18))

    print((lambda p, q: p * q)(5, 12))

    higher_order_function1 = lambda z, function1: z + function1(z)
    print("Solution for the higher order function 1 is", higher_order_function1(12, lambda z: z * z))

    higher_order_function2 = lambda  a, b, c, function2: function2(a, b) + c
    print("Solution for the second higher order function is ", higher_order_function2(2,3,4, lambda a, b: a * b))
if __name__ == '__main__':
    main()
