from dataclasses import dataclass, field
from tqdm import tqdm

@dataclass(order=True)
class Item:
	sum_freq:int = field(init=False, default=1)
	_id:int
	n1:int
	n2:int
	n3:int
	n4:int
	n5:int
	somme:int = field(init=False)
	group:str = field(init=False)
	comb_freq:int = field(init=False, default=1)

	def __post_init__(self):
		self.n1 = int(self.n1)
		self.n2 = int(self.n2)
		self.n3 = int(self.n3)
		self.n4 = int(self.n4)
		self.n5 = int(self.n5)
		self._id = int(self._id)

		self.g1 = self.n1//10
		self.g2 = self.n2//10
		self.g3 = self.n3//10
		self.g4 = self.n4//10
		self.g5 = self.n5//10

		self.somme = self.n1+self.n2+self.n3+self.n4+self.n5
		self.group = f"{self.g1}{self.g2}{self.g3}{self.g4}{self.g5}"

	def __str__(self):
		return f"{self._id};{self.n1};{self.n2};{self.n3};{self.n4};{self.n5};{self.group};{self.comb_freq};{self.somme};{self.sum_freq}"

with open(f"inputs/16_10_2022.txt") as file:
	# title = file.readline()
	title = "sep=;\nID;C1;C2;C3;C4;C5;COMB;FREQ COMB;SUM;FREQ SUM"
	lines = file.readlines()
	with open(f"output/16_10_2022.csv", "w") as f_founds:
		items = []
		print("purifying lines...")
		sum_freq = dict()
		comb_freq = dict()
		for line in tqdm(lines):
			_id, line = line.split("\t")
			list_line = line.split("-")
			if len(list_line) < 2  : continue
			item = Item(_id, *[x for x in list_line])
			items.append(item)
			if(item.somme in sum_freq):
				sum_freq[item.somme] += 1
			else:
				sum_freq[item.somme] = 1
			if(item.group in comb_freq):
				comb_freq[item.group] += 1
			else:
				comb_freq[item.group] = 1

		print("adding frequencies...")
		for i, item in tqdm(enumerate(items)):
			item.sum_freq = sum_freq[item.somme]
			item.comb_freq = comb_freq[item.group]
			# items[i] = item
		print("sorting...")
		items = sorted(items, reverse=True)
		print("exporting...")
		print(title, file=f_founds)
		for item in tqdm(items):
			print(item, file=f_founds)
	