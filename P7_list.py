def main():
    sports = ["cricket", "badminton", "basket ball", "tennis"]
    print(sports)
    print(sports[0])

    # modify the sports
    sports[2] = "soccer"
    print(sports)

    # append
    sports.append("running")
    print(sports)

    # remove
    sports.remove("running")
    print(sports)

    # remove the last one
    sports.pop()
    print(sports)

    # insert : add new element at a given index
    sports.insert(2, "kungfu")
    print(sports)

    # sort
    sports.sort()
    print(sports)

    # clear
    sports.clear()
    print(sports)


if __name__ == '__main__':
    main()
