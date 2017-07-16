import os
import zipfile


def get_dir():
    print('''Enter the location with zipped file
        for example:  /home/username/Documents/zipped''')
    location = input('..')
    if location:
        return location
    else:
        print("Please enter the location")


def unzip_files():
    location = get_dir()
    for zipped_file in os.listdir(location):
        os.chdir(location)
        if zipped_file.endswith('.zip'):
            file_unzipped = zipfile.ZipFile(zipped_file)
            file_unzipped.extractall()
            file_unzipped.close()
            print(zipped_file + " successfuly extracted.")


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
