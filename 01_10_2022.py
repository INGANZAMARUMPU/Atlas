from dataclasses import dataclass, field
from tqdm import tqdm

@dataclass(order=True)
class Item:
	sort_index:int = field(init=False, repr=False)
	n1:int
	n2:int
	n3:int
	n4:int
	n5:int
	total:int = field(init=False)
	count:int = field(init=False, default=1)

	def __post_init__(self):
		self.total = self.n1+self.n2+self.n3+self.n4+self.n5
		self.sort_index = self.total

	def __str__(self):
		f = f"{self.n1}, {self.n2}, {self.n3}, {self.n4}, {self.n5}, {self.total}, {self.count}"
		return "{"+f+"}"

with open(f"inputs/01_10_2022.txt") as file:
	lines = file.readline().split("}, {")
	with open(f"output/01_10_2022.txt", "w") as f_founds:
		items = []
		print("purifying lines...")
		for line in tqdm(lines):
			line = line.replace("{", "").replace("},", "").split(", ")
			items.append(Item(*[int(x) for x in line]))
		print("sorting...")
		items = sorted(items)
		print("affectation...")
		affectations = dict()
		for item in tqdm(items):
			if(item.total in affectations):
				affectations[item.total] += 1
			else:
				affectations[item.total] = 1
		print("exporting...")
		for item in tqdm(items):
			item.count = affectations[item.total]
			print(item, end=", ", file=f_founds)
	