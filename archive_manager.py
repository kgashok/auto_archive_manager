import os
import zipfile


dir_location = []


def get_dir():
    print('''Enter the location with zipped file
        for example:  /home/username/Documents/zipped''')
    location = input('..')
    if location:
        dir_location.append(location)
    else:
        print("Please enter the location")


def delete_zipped_files():
    location = get_dir()

    for file in os.listdirs(location):
        if file.endswith('.zip'):
            print(file)


def unzip_files():
    location = get_dir()
    for zipped_file in os.listdir(location):
        os.chdir(location)
        if zipped_file.endswith('.zip'):
            file_unzipped = zipfile.ZipFile(zipped_file)
            file_unzipped.extractall()
            file_unzipped.close()
            print(zipped_file + " successfuly extracted.")

    print('''Do you want to move or deleted the zipped files?
                Enter : 1. Delete all zipped files
                        2. Move all zipped files into one folder
                        3. Do nothing
            ''')
    choice = int(input('..'))
    if choice == 1:
        delete_zipped_files()


def get_action():
    print('''Do you want to zip or unzip files.
          Enter:
               1. zip
               2.unzip
          ''')
    action = int(input('..'))

    if action == 1:
        print("not yet implemented")
    else:
        unzip_files()

get_action()
