# here we use shutil function
# copyfile ()   : copy content of a file
# copy ()       : copyfile() + permission mode + destination can be a directory
# copy2()       : copy() +  copies metadata (file's creation and modification time)

import shutil


def main():
    shutil.copyfile("test.txt", "testcopy.txt")

    with open("testcopy.txt") as copy:
        print(copy.read())

        shutil.copyfile("test.txt", r"/Users/jayanthasenawiratne/Documents/my_venv/test21.txt")

    with open(r"/Users/jayanthasenawiratne/Documents/my_venv/test21.txt") as file_mode:
        print(file_mode.read())


if __name__ == '__main__':
    main()
