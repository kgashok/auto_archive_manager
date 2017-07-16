def get_dir():
	print('''Enter the location with zipped file
		for example:  /home/username/Documents/zipped''')
	location = input('..')
	if location:
		return location
	else:
		print("Please enter the location")

get_dir()
