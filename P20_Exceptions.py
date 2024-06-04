print("Exception = event detected during execution that interrupts the flow of programs")


def main():
    numerator = int(input("Enter the number to be divided: "))
    denominator = int(input("Enter the number to be divided by: "))
    answer = numerator / denominator
    print(answer)
    try:
        numerator = int(input("Enter the number to be divided: "))
        denominator = int(input("Enter the number to be divided by: "))
        answer = numerator / denominator
        print(answer)

    except:
        print("Error: program terminated")

    try:
        numerator = int(input("Enter the number to be divided: "))
        denominator = int(input("Enter the number to be divided by: "))
        answer = numerator / denominator
        print(answer)
    except ZeroDivisionError:
        print("Error: denominator cannot be zero")
    except ValueError:
        print("Error: value cannot be a letter")
    except Exception:
        print("Error: unknown")

    try:
        numerator = int(input("Enter the number to be divided: "))

        denominator = int(input("Enter the number to be divided by: "))

        answer = numerator / denominator

        print(answer)
    except ZeroDivisionError as e:
        print(e)
        print("Error")
    except ValueError as e:
        print(e)
        print("Error")
    else:
        print("Answer")
    finally:  # this is useful when we do file handling
        print("This is always executes")


if __name__ == '__main__':
    main()
