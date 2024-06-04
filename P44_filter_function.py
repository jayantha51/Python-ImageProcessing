# filter() = creates collection of elements from an iterable for which a function returns True
# filter (function, iterable)

def main():
    friends = [("JS", 15),
               ("BS", 16),
               ("KA", 8),
               ("JA", 99)]
    limit_age = lambda data: data[1] >= 13
    teen_friends = list(filter(limit_age, friends))
    print(teen_friends[0][0])
    print("Next__________")

    for i in range(3):
        print(teen_friends[i][0])

    print("one can print everything in the list as follow")
    for i in teen_friends:
        print(i)


if __name__ == '__main__':
    main()
