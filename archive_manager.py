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

unzip_files()
