from dataclasses import dataclass, field
from tqdm import tqdm

@dataclass(order=True)
class Item:
	index:int
	n1:int
	n2:int
	n3:int
	n4:int
	n5:int
	value:int = field(init=False)

	def __post_init__(self):
		self.value = f"{self.n1}{self.n2}{self.n3}{self.n4}{self.n5}"

	def __str__(self):
		return f"{self.n1};{self.n2};{self.n3};{self.n4};{self.n5};{self.index}".replace("\n","")

srcs = dict()
dests = dict()
title = "sep=;\nC1;C2;C3;C4;C5;FOUND"

print("reading sources...")
with open(f"inputs/23_10_2022_src.csv") as file:
	file.readline()
	for line in tqdm(file.readlines()):
		item = Item(*line.split(";"))
		srcs[item.value] = item

print("reading destinations...")
with open(f"inputs/23_10_2022_dest.csv") as file:
	file.readline()
	for line in tqdm(file.readlines()):
		item = Item(*line.split(";"))
		dests[item.value] = item

print("founding combinations...")
for key in tqdm(dests.keys()):
	if key in srcs:
		dests[key].index = srcs[key].index

print("sorting results...")
items = sorted(list(dests.values()))

print("exporting results...")
with open(f"output/23_10_2022.csv", "w") as f_founds:
	print(title, file=f_founds)
	for item in tqdm(items):
		print(item, file=f_founds)
	