def main():

    Time  = 3

    print("I can meet with you "+str(Time) +" pm Tomorrow")
    your_name = input("please enter your name: ")
    print("upper case: ", your_name.upper())
    print("capitalized: ", your_name.capitalize())
    age = str(input("enter you age: "))
    print("Hi "+your_name.capitalize()+"you are "+ age+ " years old")
if __name__ == '__main__':
    main()