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
			comb = "-".join(combination)
			if comb in dict_combination:
				dict_combination[comb]+=1
			else:
				dict_combination[comb] = 1

	print("writting results")
	file = open("output/17_11_2022.csv", 'w')
	for line in tqdm(lines):
		list_line = line[:-1].split(";")
		combinations = list(itertools.combinations(list_line, 2))
		entire_comb = ""
		for combination in combinations:
			comb = "-".join(combination)
			entire_comb += f"{comb};{dict_combination[comb]};"
		print(f"{line[:-1]};{entire_comb}", file=file)
	file.close()