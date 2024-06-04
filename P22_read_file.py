def main():
    with open(r"/Users/jayanthasenawiratne/Documents/my_venv/test.txt") as file:
        print(file.read())
    print("\n")

    with open(r"/Users/jayanthasenawiratne/Documents/my_venv/test.txt") as file2:
        print(file2.read())
        print(file2.close())
    print("\n")

    try:
        with open(r"/Users/jayanthasenawiratne/Documents/my_venv/test.txt") as file3:
            print(file3.read())
    except FileNotFoundError:
        print("file cannot be found")


if __name__ == '__main__':
    main()
