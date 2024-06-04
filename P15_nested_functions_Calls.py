print("functions call inside other function calls"
      "innermost function call area resolved first"
      "returned values is used as a argument"
      "for the next out functionss")


def main():
    number = input("Enter a number:")
    number = float(number)
    number = abs(number)
    number = round(number)
    print(number)

    print(round(abs(float(number))))


if __name__ == '__main__':
    main()
