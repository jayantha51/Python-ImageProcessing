print("args = parameter that will pack all arguments into a tuple"
      "useful so that function accepts a varying amount of arguments")


def main():
    def add_function1(n1, n2):
        sum = n1 + n2
        return sum

    # this function cannot handle more than one input
    print(add_function1(1, 2))

    def add_function2(*args):
        sum = 0

        for i in args:
            sum += i
        return sum

    print(add_function2(1, 2, 3))

    def sub_function(*var):
        answer = 0
        for i in var:
            answer -= i
        return answer

    print(sub_function(6, 2, 3))

    def add(*stuff):
        sum = 0
        stuff = list(stuff)
        stuff[0] = 0
        for i in stuff:
            sum += i
        return sum

    print(add(1, 2, 3))
    print(add(3, 4, 121))  # oth element always 0 since it is defined in the function


if __name__ == '__main__':
    main()
