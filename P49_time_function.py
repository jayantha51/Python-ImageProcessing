import time


def main():
    print(time.ctime(0))  # convert a time expressed in seconds since epoch to readable string
    # epoch = when your computer thninks time began (reference point)
    print(time.time())  # return current seconds since epoch
    print(time.ctime(time.time()))  # get current time
    print("next line________________")
    time_object = time.localtime()  # not readable
    print(time_object)
    time_object = time.strftime("%B %d %Y %H:%M:%S", time_object)
    print(time_object)

    time_string = "20 April, 2020"
    time_object = time.strptime(time_string, "%d %B, %Y")
    print(time_object)

    # (year, month, day, hours,  minutes, secs, # day of the week, # day of the year, dst)
    time_tuple= (2020, 4, 20, 4, 20, 0, 0, 0, 0)
    time_string = time.asctime(time_tuple)
    print(time_string)

    # (year, month, day, hours, minutes, secs, #day of the week, # day of the year, dst)
    time_tuple =  (2020, 4, 20, 4, 20, 0, 0, 0, 0)
    time_string = time.mktime(time_tuple)
    print(time_string)


if __name__ == '__main__':
    main()
