from datetime import date, timedelta
from dataclasses import dataclass
from tqdm import tqdm

@dataclass(order=True)
class Item:
	old_date:str
	combination:str
	new_date:str

	def __post_init__(self):
		self.old_date = self.old_date
		self.combination = self.combination
		self.new_date = self.new_date

	def __str__(self):
		return f"{self.old_date};{self.combination};{self.new_date}"

with open(f"inputs/22_01_2023.csv") as file:
	lines = file.readlines()
	with open(f"output/22_01_2023.csv", "w") as f_founds:
		items = []
		print("purifying lines...")
		day = date(day=20, month=9, year=1996)
		for line in tqdm(lines):
			line = line[:-1].split(";")
			if len(line) < 2  : continue
			items.append(Item(*[x for x in line], f'{day.strftime("%A")}, {day}'))
			day = day+timedelta(days=1)
		print("exporting...")
		print("sep=;", file=f_founds)
		for item in tqdm(items):
			print(item, file=f_founds)
	