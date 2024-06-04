def main():
    name  = "Pi Charm"
    print(name[0])
    print("first name: ",name[:2])
    print("last name: ", name[3:])
    print("reverse name: ", name[::-1])
    website1 = "http://apple.com"
    website2 = "http://google.com"
    slice1 = slice(7,-4)
    print(website1[slice1])
    print(website2[slice1])
    your_name = input("enter your name: ")
    print("you name in reverse order: ", your_name[::-1])

if __name__ == '__main__':
    main()