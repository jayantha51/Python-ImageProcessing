def main():
    with open ('test1.txt') as fp1:
        data1 = fp1.read()
        print(data1)

    with open ('test2.txt') as fp2:
        data2 = fp2.read()
        print(data2)

    data = data1 + "\n" + data2

    with open ('test.txt', 'w') as fp:
        fp.write(data)
        fp.close()

if __name__ == '__main__':
    main()