from dataclasses import dataclass, field
from tqdm import tqdm

@dataclass(order=True)
class Item:
	freq:int = field(init=False, default=1)
	_id:int
	n1:int
	n2:int
	n3:int
	n4:int
	n5:int
	somme:int = field(init=False)

	def __post_init__(self):
		self.n1 = int(self.n1)
		self.n2 = int(self.n2)
		self.n3 = int(self.n3)
		self.n4 = int(self.n4)
		self.n5 = int(self.n5)
		self._id = int(self._id)
		self.somme = self.n1+self.n2+self.n3+self.n4+self.n5

	def __str__(self):
		return f"{self._id};{self.n1};{self.n2};{self.n3};{self.n4};{self.n5};{self.somme};{self.freq}"

with open(f"inputs/16_10_2022.txt") as file:
	# title = file.readline()
	title = "sep=;\nID;C1;C2;C3;C4;C5;SOMME;FREQ"
	lines = file.readlines()
	with open(f"output/16_10_2022.csv", "w") as f_founds:
		items = []
		print("purifying lines...")
		counts = dict()
		for line in tqdm(lines):
			_id, line = line.split("\t")
			list_line = line.split("-")
			if len(list_line) < 2  : continue
			item = Item(_id, *[x for x in list_line])
			items.append(item)
			if(item.somme in counts):
				counts[item.somme] += 1
			else:
				counts[item.somme] = 1

		print("adding frequencies...")
		for i, item in tqdm(enumerate(items)):
			item.freq = counts[item.somme]
			# items[i] = item
		print("sorting...")
		items = sorted(items, reverse=True)
		print("exporting...")
		print(title, file=f_founds)
		for item in tqdm(items):
			print(item, file=f_founds)
	