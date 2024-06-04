# multiprocessing = running tasks in parallel on different cpu cores, bypass GIL used for threading
#                   multiprocessing= better for cpu bound tasks (heavy cpu usage)
#                   multiprocessing = better for io bound tasks (waiting around)

# processing time for this code is 43.2 seconds
from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    print(cpu_count())  # prints how many cpu-counts available
    a = Process(target=counter, args=(1000000000,))
    a.start()
    a.join()
    print("finished in :", time.perf_counter(), "seconds")


if __name__ == '__main__':
    main()
# need to recheck this program