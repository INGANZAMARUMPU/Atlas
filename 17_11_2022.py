import itertools # combinations(list, size) or permutations(list, size)
from tqdm import tqdm

dict_combination = {}

with open("inputs/17_11_2022.csv", "r") as db:
	print("reading and parsing raw data")
	lines = db.readlines()
	for line in tqdm(lines):
		list_line = line[:-1].split(";")
		combinations = list(itertools.combinations(list_line, 2))
		for combination in combinations:
			comb = ";".join(combination)
			if comb in dict_combination:
				dict_combination[comb].append("-".join(list_line))
			else:
				dict_combination[comb] = []

	print("writting results")
	file = open("output/17_11_2022.csv", 'w')
	for key in tqdm(dict_combination):
		values = dict_combination[key]
		str_values = ";".join(values)
		print(f"{key};{len(values)};{str_values}", file=file)
	file.close()