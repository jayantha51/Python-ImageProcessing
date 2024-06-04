# High order function = a function that either
# 1. accepts a function as an argument
# or 2. returns a function (in python, functions are also treated as objects)

def main():
    # example 1:
    def loud(text):
        return text.upper()

    def quiet(text):
        return text.lower()

    def demo1(function1):
        res = function1("hEllo")
        print(res)

    demo1(loud)
    demo1(quiet)

    # example 2
    def add(num):
        return num + 10

    def sub(num):
        return num - 10

    def demo2(function2):
        new = function2(3 + 5)
        return new

    # example 3
    print(demo2(add))
    print(demo2(sub))

    def divisor(x):
        def dividend(y):
            return y / x

        return dividend

    divide = divisor(2)
    print(divide(10))

    # example 4

    def demoFunction (c, d):
        print("multiplication is", c * d)

    def outerFunction(sample):
        def innerFunction(c,d):
            return sample(c,d)
        return innerFunction

    demoFunction = outerFunction(demoFunction)
    demoFunction(5,7)

if __name__ == '__main__':
    main()
