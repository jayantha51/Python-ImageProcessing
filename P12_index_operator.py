print("index operator []: gives access to a sequence's elements (str,list, tuple)")


def main():
    name = "pi charm"

    if (name.islower()):
        name = name.upper()
    print(name)

    first_name = name[:2].capitalize()
    print(first_name)
    last_name =  name[3:].capitalize()
    print(last_name)

    print("last letter of the name is:", name[-1])
    
if __name__ == '__main__':
    main()
