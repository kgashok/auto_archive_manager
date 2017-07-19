# Script Name : auto_archives_manager.py
# Author      : Stanley Ulili
# Created     : July 16 2017
# Version     : 0.1

# Description : This is a script that unzip all zipped files in a directory.
#               It allows you to delete or move the zipped files after
#               extraction.

import os
import sys
import re
import shutil
import zipfile


def get_dir():
    """ Get the location of folder with zipped files from the user"""
    print('''Enter the location of the folder with zipped files

             /home/username/Documents/folder with zipped files on unix
                       or
             C:/Users/username/Desktop/folder with zipped files on Windows
             enter 'q' to quit.
          ''')

    location = input('..')
    if location:
        if location.lower() == 'q':
            sys.exit()
        else:
            return location
    else:
        print("Please enter the location")


dir_location = get_dir()


def delete_zipped_files():
    """ Delete the zipped files in the folder"""
    for file in os.listdir(dir_location):
        if file.endswith('.zip'):
            os.unlink(file)
    print("program finished.")


def move_zipped_files():
    """ Move zip files to a folder zipped_files """
    try:
        os.makedirs('zipped_files')
        for file in os.listdir(dir_location):
            if file.endswith('.zip'):
                shutil.move(file, 'zipped_files')
    except FileExistsError:
        print("folder named zipped_files already exists")
        print("Would the files moved into the zipped_files directory? Y/N")
        response = input('..')
        if response.lower() == 'y':
            for file in os.listdir(dir_location):
                if file.endswith('.zip'):
                    shutil.move(file, 'zipped_files')
            print("program finished.")
        else:
            sys.exit()
    else:
        print("zipped files move to 'zipped_files' directory")


def zip_files():
    """ Creates zip archives """
    os.chdir(dir_location)
    for file in os.listdir(dir_location):
        if file.endswith('.zip'):
            pass
        else:
            zipped_file = zipfile.ZipFile(file + '.zip', 'w')
            zipped_file.write(file, compress_type=zipfile.ZIP_DEFLATED)
            zipped_file.close()
            print(file + " successfully zipped.")


def unzip_files():
    """ Unzips archives and also call other functions to delete or move
    the zipped files """
    os.chdir(dir_location)        # get into the folder with zipped files
    pattern = re.compile(r'([\w ]+)\.[^\.]+$')  # Match name without .zip
    for zipped_file in os.listdir(dir_location):
        if zipped_file.endswith('.zip'):
            match = pattern.search(zipped_file)
            file_unzipped = zipfile.ZipFile(zipped_file)
            file_unzipped.extractall(match.group(1))
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
    elif choice == 2:
        move_zipped_files()
    else:
        sys.exit()


def get_action():
    """ Let's the user choose whether to zip or unzip files"""
    print('''Do you want to zip or unzip files.
          Enter:
               1. zip
               2.unzip
          ''')
    action = int(input('..'))

    if action == 1:
        zip_files()
    else:
        unzip_files()

get_action()
