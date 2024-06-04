#  daemon thread = a thread that runs in te background, now important for program to run
#                   your program will not wait for daemon threads to complete before existing
#                   non-daemon threads cannot normally be killed, stay active until task is complete
#                   ex. background, garbage collection, waiting for input, long running process

import threading
import time

def timer():
    Count = 0
    while True:
        time.sleep(1)
        Count += 1
        print("Logged time is ", Count, "seconds")

def main():
    x = threading.Thread(target=timer(), daemon=True)
    x.start()

    answer = input("Do you want to exit: \n")
    print("is this a damon thread: ", x.isDaemon())
if __name__ == '__main__':
    main()