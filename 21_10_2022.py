from dataclasses import dataclass, field
from tqdm import tqdm

@dataclass(order=True)
class Item:
	n1:int
	n2:int
	n3:int
	n4:int
	n5:int
	g_index:int
	l_index:int = field(init=False, default=-1)

	def __str__(self):
		return f"{self.n1};{self.n2};{self.n3};{self.n4};{self.n5};{self.l_index};{self.g_index}"

with open(f"inputs/21_10_2022.txt") as file:
	# title = file.readline()
	title = "sep=;\nC1;C2;C3;C4;C5;LOCAL;GLOBAL"
	lines = file.readline().split("}, {")

	items = []
	for i, line in enumerate(tqdm(lines)):
		line = line.replace("{", "").replace("},", "").split(", ")
		item = Item(*line, i)
		items.append(item)

	print("exporting 100_000...")
	for a in range((len(items)//100_000)+1):
		min_range = a*100_000
		max_range = (a+1)*100_000

		with open(f"output/21_10_2022_{min_range}-{max_range-1}.csv", "w") as f_founds:
			print(title, file=f_founds)
			for i, b in enumerate(tqdm(items[min_range:max_range])):
				item = items[min_range+i]
				item.l_index = i
				print(item, file=f_founds)

	print("exporting 1000_000...")
	for a in range((len(items)//1000_000)+1):
		min_range = a*1000_000
		max_range = (a+1)*1000_000

		with open(f"output/21_10_2022_{min_range}-{max_range-1}.csv", "w") as f_founds:
			print(title, file=f_founds)
			for i, b in enumerate(tqdm(items[min_range:max_range])):
				item = items[min_range+i]
				item.l_index = i
				print(item, file=f_founds)
	