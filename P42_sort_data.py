# sort() method = used with lists so if we have a Tuple the sort method won't work
# sort() function  = used with iterable

def main():
    student = ["D", "HA", "OF", "GAS", "KA"]
    student.sort(reverse=True)
    for x in student:
        print(x)
    print(student)

    print("Next _____________________")
    candidates = ("HH", "AHA", "LA", "GAHA")
    sorted_candidates = sorted(candidates,reverse=True)
    for i in sorted_candidates:
        print(i)
    # Let's try a different example
    new_comers = [("HA", "F", 37),
                  ("HAG", "A", 32),
                  ("UA", "B", 22),
                  ("BA", "D", 56)]
    print("next2_____________________")
    grade = lambda grades: grades[1]
    new_comers.sort(key=grade, reverse=True)
    for a in new_comers:
        print(a)

    print("Next3___________________")
    age = lambda ages: ages[2]
    new_comers.sort(key = age)
    for i in new_comers:
        print(i)

    print("Next4___________________")
    new_comers = [("HA", "F", 37),
                  ("HAG", "A", 32),
                  ("UA", "B", 22),
                  ("BA", "D", 56)]

    sorted_new_comers = sorted(new_comers, key=age)
    for i in sorted_new_comers:
        print(i)

if __name__ == '__main__':
    main()