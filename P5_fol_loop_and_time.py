import time

def main():
    for i in range (10,0,-1):
        print(i)

    for i in "charm":
        print(i)

    for seconds in range (10,0,-1):
        print(seconds)
        time.sleep(1)
    print("HAPPY NEW YEAR!!!")


if __name__ == '__main__':
    main()