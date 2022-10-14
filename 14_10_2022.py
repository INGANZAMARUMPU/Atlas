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
	somme:int
	freq:int
	group:str = field(init=False)
	group_freq:int = field(init=False, default=1)

	def __post_init__(self):
		self.n1 = int(self.n1)
		self.n2 = int(self.n2)
		self.n3 = int(self.n3)
		self.n4 = int(self.n4)
		self.n5 = int(self.n5)
		self.somme = int(self.somme)

		self.g1 = self.n1//10
		self.g2 = self.n2//10
		self.g3 = self.n3//10
		self.g4 = self.n4//10
		self.g5 = self.n5//10

		self.group = f"{self.g1}{self.g2}{self.g3}{self.g4}{self.g5}"
		self.sort_index = self.group

	def __str__(self):
		return f"{self.n1};{self.n2};{self.n3};{self.n4};{self.n5};{self.somme};{self.freq};{self.group};{self.group_freq}"

with open(f"inputs/14_10_2022.csv") as file:
	title = file.readline()[:-1]+"groups;frequence groups"
	lines = file.readlines()
	with open(f"output/14_10_2022.csv", "w") as f_founds:
		items = []
		print("purifying lines...")
		counts = dict()
		for line in tqdm(lines):
			line = line.split(";")[:-1]
			if len(line) < 2  : continue
			item = Item(*[x for x in line])
			items.append(item)
			if(item.group in counts):
				counts[item.group] += 1
			else:
				counts[item.group] = 1

		print("sorting...")
		items = sorted(items)
		print("exporting...")
		print("sep=;", file=f_founds)
		print(title, file=f_founds)
		for item in tqdm(items):
			item.group_freq = counts[item.group]
			print(item, file=f_founds)
	