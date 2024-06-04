from pathlib import Path


def main():
    file_path = Path.home() / 'Desktop/sub_folder/file.jpeg'
    print(file_path)
    print(file_path.name)
    print(file_path.parent.parent.name)
    print(file_path.suffix)
    backup_file_path = file_path.parent / (file_path.stem + ' backup' + file_path.suffix)
    print(backup_file_path)

if __name__ == '__main__':
    main()
