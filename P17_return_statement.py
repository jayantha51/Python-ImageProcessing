def main():
    print("return statement =  functions send Python  values/objects back to the caller. "
          "These values/objects are know as the functions' return values")

    def multiply1(n1, n2):
        result = n1 * n2
        return result

    print("mulitplication value is ", multiply1(22, 5))

    x = multiply1(2, 3)
    print(x)

    def multiply2(a, b):
        return a * b

    print("multiplication is", multiply2(5, 10))


if __name__ == '__main__':
    main()
