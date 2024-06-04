print("set is collection which is unordered, un-indexed, no duplicate values, fast")


def main():
    computer_parts = {"display", "mother board", "mouse", "key board"}
    print(computer_parts)
    computer_parts.add("graphic card")
    computer_parts.remove("key board")
    print(computer_parts)

    tv_parts = {"remote controller", "display", "speakers"}
    computer_tv_parts = computer_parts.union(tv_parts)
    print(computer_tv_parts)

    computer_tv_parts_difference = computer_parts.difference(tv_parts)
    print(computer_tv_parts_difference)

    computer_tv_parts_intersection = computer_parts.intersection(tv_parts)
    print(computer_tv_parts_intersection)


if __name__ == '__main__':
    main()
