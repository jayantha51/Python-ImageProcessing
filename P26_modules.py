# module = a file containing python code. May contain functions, classes, etc.
# used with modular programming, which is to separate a program into parts
# to test this example we will need message.py

def main():
    import message as msg
    print("printing the first message")
    msg.hello()
    print("printing the second message")
    msg.bye()

    from message import hello, bye
    print("printing both messages below")
    hello()
    bye()
if __name__ == '__main__':
    main()
