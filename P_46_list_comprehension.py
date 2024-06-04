# list comprehension = way to create a new list with less syntax
#                       can mimic certain lambda function, easier to read
#                      List = [expression = for item + in iterables]
#                      List = [expression + for item in + iterable + if conditional]
#                      List = [expression if/else for item in iterable]

def main():
    squares = []  # create and empty list
    for i in range(1, 11):
        squares.append(i * i)
    print(squares)

    squares = [i * i for i in range(1, 11)]
    print(squares)

    students = [99, 82, 100, 67, 43, 78, 98, 12]
    passed_students = list(filter(lambda x: x >= 50, students))
    print(passed_students)
    # Let's try this with list comprehension
    passed_students2 = [i for i in students if i >= 50]
    print(passed_students2)

    passed_students3 = [i if i >= 50 else "FAILLED" for i in students]
    print (passed_students3)


if __name__ == '__main__':
    main()
