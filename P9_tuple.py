print("tuple = collection which is ordered and unchangeable"
      "used to group together related data")

def main():
    users = ("age", "country", "name", "name")
    print(users.count("name"))
    print(users.index("country"))
    print(len(users))

    for x in users:
        print(x)


    new_name = "name"
    if new_name in users:
        print(new_name+ " is in the list")
    else:
        print(new_name+" not in the list")

if __name__ == '__main__':
    main()