import csv
import re
import os
import time
import glob

# Will run conversion on all .csv files in this directory
def allLocalFiles():
	print(f"name\tstart size\time seconds")
	for csv_file in glob.glob("*.csv"):
		time = convertCSVtoCOPL(csv_file)
		file_size = os.path.getsize(csv_file)
		print(f"{csv_file}\t{file_size}\t{time:.2f}")

# Conversion function for each .csv file
def convertCSVtoCOPL(csv_file):
	total_rows = 0

	start = time.time()
	# Gets folder name from csv
	new_folder_name = os.path.splitext(csv_file)[0]
	if(not os.path.isdir(new_folder_name)):
		os.mkdir(new_folder_name)

	# Finds the total rows in the file
	with open(csv_file, 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			if (len(row) > total_rows):
				total_rows = len(row)

	# Writes rows to new files
	for i in range(0,total_rows):
		with open(csv_file, 'r') as file:
			reader = csv.reader(file)
			column_file = os.path.join(new_folder_name, f"column{i+1}.txt")
			if (os.path.exists(column_file)):
				os.remove(column_file)
			f = open(column_file, "a")
			for row in reader:
				f.write(row[i]+"\n")
			f.close()
	end = time.time()
	return end - start

def convertCSVtoCOPLpandas(csv_file):
	total_rows = 0

	start = time.time()
	# Gets folder name from csv
	new_folder_name = os.path.splitext(csv_file)[0]
	if(not os.path.isdir(new_folder_name)):
		os.mkdir(new_folder_name)

	# Finds the total rows in the file
	with open(csv_file, 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			if (len(row) > total_rows):
				total_rows = len(row)

	# Writes rows to new files
	for i in range(0,total_rows):
		with open(csv_file, 'r') as file:
			reader = csv.reader(file)
			column_file = os.path.join(new_folder_name, f"column{i+1}.txt")
			if (os.path.exists(column_file)):
				os.remove(column_file)
			f = open(column_file, "a")
			for row in reader:
				f.write(row[i]+"\n")
			f.close()
	end = time.time()
	return end - start

allLocalFiles()