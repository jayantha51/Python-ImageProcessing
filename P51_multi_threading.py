# thread = a flow of executions. like a separate order of instructions.
#          however each thread takes a turn running to achieve concurrency
#          GIL = (global interpreter lock)
#          Allow only one thread to hold the control of the Python interpreter at any one time

# cpu = program/task spand most of it's time waiting for internal events (cpu intensive)
#   use multiprocessing

# io bound = program/tak spends most of it's time waiting for external events (user input, webs scraping)
#            use multithreading

import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("you eat breakfast")


def drink_tea():
    time.sleep(4)
    print("you drink tea")


def watch_news():
    time.sleep(5)
    print("you are done watching news")


def main():
    x = threading.Thread(target=eat_breakfast(), args=())
    x.start()
    y = threading.Thread(target=drink_tea(), args=())
    y.start()
    z = threading.Thread(target=watch_news(), args=())
    z.start()
    # This will take 5 seconds to complete the program (because it uses multithreading)
    print(threading.active_count())
    print(threading.enumerate())
    print(time.process_time())
    print(time.perf_counter())


if __name__ == '__main__':
    main()
