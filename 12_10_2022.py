from dataclasses import dataclass, field
from tqdm import tqdm

@dataclass(order=True)
class Item:
	sort_index:int = field(init=False, repr=False)
	date:str
	n1:int
	n2:int
	n3:int
	n4:int
	n5:int
	total:int = field(init=False)

	def __post_init__(self):
		self.n1 = int(self.n1)
		self.n2 = int(self.n2)
		self.n3 = int(self.n3)
		self.n4 = int(self.n4)
		self.n5 = int(self.n5)
		list_date = self.date.split("/")
		self.date = f"{list_date[1]}/{list_date[0]}/{list_date[2]}"
		self.total = self.n1+self.n2+self.n3+self.n4+self.n5
		self.sort_index = self.total

	def __str__(self):
		return f"{self.date},{self.n1},{self.n2},{self.n3},{self.n4},{self.n5},{self.total}"

with open(f"inputs/12_10_2022.txt") as file:
	lines = file.readlines()
	with open(f"output/12_10_2022.csv", "w") as f_founds:
		items = []
		print("purifying lines...")
		for line in tqdm(lines):
			line = line.split(",")
			if len(line) < 2  : continue
			items.append(Item(*[x for x in line]))
		print("sorting...")
		items = sorted(items)
		print("exporting...")
		print("sep=,", file=f_founds)
		for item in tqdm(items):
			print(item, file=f_founds)
	