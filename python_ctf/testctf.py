from ctf import Ctf

ctf_file = Ctf("ignore_country_classification")
for item in ctf_file["column1"]:
	print(item)
col =  ctf_file["column1"]
print(list(col))
print(len(col))


# # Runs repeatedly with an additional column until the search goes through everything
# converter = Ctf()
# for i in range(1,16):
# 	start = time.time()
# 	columns_to_search = []
# 	for column in range(1, i+1):
# 		columns_to_search.append(f'column{column}.txt')
# 	rows = converter.load_columns("ignore_test", columns_to_search)
# 	end = time.time()
# 	print(f'Searched {len(columns_to_search)} columns with {len(rows[0])} rows in {(end-start):.2f} seconds')

# converter.convert_local_files()