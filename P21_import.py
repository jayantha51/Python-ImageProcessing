import os

print("checking if file exists in a folder")


def main():
    file_name = r"/Users/jayanthasenawiratne/Documents/my_venv/test.txt"
    if os.path.exists(file_name):
        print("file location exists")
        if os.path.isfile(file_name):
            print("file exists")
    else:
        print("file does not exists")
    print("next_______________________________")
    file_folder = r"/Users/jayanthasenawiratne/Documents/my_venv/"

    if os.path.exists(file_folder):
        if os.path.isfile(file_folder):
            print("this is a file")
        elif os.path.isdir(file_folder):
            print("this is a folder")
    else:
        print("file folder does not exists")


if __name__ == '__main__':
    main()
