# map() = applies a function to each item in and iterable (list, tuple, etc.)
# map (function, iterable): mainly there are two arguments

def main():
    store = [("shirt", 22.00),
             ("short", 12.00),
             ("pants", 73.50),
             ("shoes", 55.75)]
    convert_to_slr = lambda data: (data[0], data[1]*302)

    stor_to_slr = list(map(convert_to_slr,store))

    for i in stor_to_slr:
        print(i)
if __name__ == '__main__':
    main()