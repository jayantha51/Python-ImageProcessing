import os
def main():
    file =  r"/Users/jayanthasenawiratne/Documents/my_venv/test.txt"

    try:
        os.remove(file) # the same argument can be use to delete folder also
    except FileNotFoundError:
        print("File not found")
    else:
        print(file, "deleted")
if __name__ == '__main__':
    main()
