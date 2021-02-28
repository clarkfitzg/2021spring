import csv
import os
import time
import glob

class Copl:
	'''
	This class will be used to convert to and from Copl files
	'''

	def allLocalFiles(self):
		'''Will run conversion on all .csv files in this directory'''
		print(f'name\tstart size\time seconds')
		for csv_file in glob.glob('*.csv'):
			time = self.convertCSVtoCOPL(csv_file)
			file_size = os.path.getsize(csv_file)
			print(f'{csv_file}\t{file_size}\t{time:.2f}')

	def convertCSVtoCOPL(self, csv_file):
		'''Conversion function for each .csv file'''
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
				column_file = os.path.join(new_folder_name, f'column{i+1}.txt')
				if (os.path.exists(column_file)):
					os.remove(column_file)
				f = open(column_file, 'a')
				for row in reader:
					f.write(row[i]+'\n')
				f.close()
		end = time.time()
		return end - start

	def loadColumns(self, copl_file, columns):
		'''
		file: the name of the folder what contains the columns
		columns: column names to return
		returns a list with the column values in it
		'''
		return_list = []
		for column in columns:
			return_list.append(self.loadColumn(copl_file, column))
		return return_list

	def loadColumn(self, copl_file, column):
		return_list = []
		# Get full path to copl column
		column_file = os.path.join(copl_file, column)
		# Finds the total rows in the file
		with open(column_file, 'r') as file:
			reader = csv.reader(file, delimiter='\n')
			for line in reader:
				try:
					return_list.append(line[0])
				except Exception as e:
					continue
		return return_list

# Runs repeatedly with an additional column until the search goes through everything
converter = Copl()
for i in range(1,16):
	start = time.time()
	columnsToSearch = []
	for column in range(1, i+1):
		columnsToSearch.append(f'column{column}.txt')
	rows = converter.loadColumns("ignore_test", columnsToSearch)
	end = time.time()
	print(f'Searched {len(columnsToSearch)} columns with {len(rows[0])} rows in {(end-start):.2f} seconds')