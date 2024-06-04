def main():
    year = ["2023", "1999", "1972", "1971"]
    month = ["May", "March", "July", "April"]
    day = ["Friday", "Tuesday", "Monday"]
    ymd = [year, month, day]
    print(ymd)
    print(ymd[0][1])
    print(ymd[1][1])
    print(ymd[2][1])

    print("list of years")
    for i in range(4):
        print(ymd[0][i])

    print("list of months")
    for i in range (4):
        print(ymd[1][i])

    print("list of days")
    for i in range(3):
        print(ymd[2][i])
if __name__ == '__main__':
    main()
