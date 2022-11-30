from dataclasses import dataclass, field
from tqdm import tqdm

@dataclass(order=True)
class Item:
	total:int = field(init=False, repr=False)
	n1:int
	n2:int
	n3:int
	n4:int

	def __post_init__(self):
		self.n1 = int(self.n1)
		self.n2 = int(self.n2)
		self.n3 = int(self.n3)
		self.n4 = int(self.n4)
		self.total = self.n1+self.n2+self.n3+self.n4

	def __str__(self):
		return f"{self.n1},{self.n2},{self.n3},{self.n4},{self.total}"

with open(f"inputs/30_11_2022.txt", 'r') as file:
	lines = file.readline().split("}, {")
	items = []
	for line in tqdm(lines):
		line = line.replace("{", "").replace("},", "").split(", ")
		if len(line) < 2  : continue
		items.append(Item(*[x for x in line]))
	print("sorting...")
	items = sorted(items)
	print("Counting")
	db = {}
	for item in tqdm(items):
		if db.get(str(item.total)):
			db[str(item.total)] += 1
		else:
			db[str(item.total)] = 1
	print("exporting...")
	with open(f"output/30_11_2022.csv", 'a') as f_founds:
		title = "sep=,\nC1,C2,C3,C4,SUM,COUNT"
		print(title, file=f_founds)
		for item in tqdm(items):
			print(item, f',{db[str(item.total)]}', sep='', file=f_founds)
