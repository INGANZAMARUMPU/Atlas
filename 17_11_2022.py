from datetime import date, timedelta
from tqdm import tqdm

dict_combination = {}

with open("inputs/17_11_2022.csv", "r") as db:
	print("reading and parsing raw data")
	lines = db.readlines()

	f_founds = open(f"output/17_11_2022.csv", "w")
	base = date(1900, 1, 1)
	for line in tqdm(lines):
		str_date = f"{base.day}/{base.month}/{base.year}"
		line = str_date+";"+line
		print(line[:-1], file=f_founds)
		base += timedelta(days=1)
	f_founds.close()
