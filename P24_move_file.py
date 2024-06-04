import os


def main():
    source = "test21.txt"
    destination = r"/Users/jayanthasenawiratne/Documents/my_venv/test.txt"
    try:
        if os.path.exists(destination):
            print("file exists")
        else:
            os.replace(source, destination)
    except FileNotFoundError:
        print("file not found")

    source_folder = "newFolder"
    destination_folder = r"/Users/jayanthasenawiratne/Documents/my_venv/"

    try:
        if os.path.exists(destination_folder):
            print(source_folder, "exists")
        else:
            os.replace(source_folder,destination_folder)
    except FileNotFoundError:
        print(source_folder, "error folder not found")



if __name__ == '__main__':
    main()
