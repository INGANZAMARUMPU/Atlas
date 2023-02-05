from dataclasses import dataclass, field
from tqdm import tqdm

@dataclass(order=True)
class Item:
	a:int
	b:int
	c:int
	d:int
	e:int

	c_1:int = field(init=False, default=0)
	c_2:int = field(init=False, default=0)
	c_3:int = field(init=False, default=0)
	c_4:int = field(init=False, default=0)
	c_5:int = field(init=False, default=0)

	def to_1(self):
		return f"{self.a}"
	def to_2(self):
		return f"{self.a}_{self.b}"
	def to_3(self):
		return f"{self.a}_{self.b}_{self.c}"
	def to_4(self):
		return f"{self.a}_{self.b}_{self.c}_{self.d}"
	def to_5(self):
		return f"{self.a}_{self.b}_{self.c}_{self.d}_{self.e}"

	def __str__(self):
		return f"{self.a};{self.b};{self.c};{self.d};{self.e};{self.c_1};{self.c_2};{self.c_3};{self.c_4};{self.c_5}"

d_1 = dict()
d_2 = dict()
d_3 = dict()
d_4 = dict()
d_5 = dict()
db = []

title = "A;B;C;D;E;A,AB,ABC,ABCD,ABCDE"

print("reading sources...")
with open(f"inputs/05_02_2023.csv") as file:
	file.readline()
	for line in tqdm(file.readlines()):
		item = Item(*[x for x in line[:-1].split(",") if x != ''])

		if item.to_1() in d_1:
			d_1[item.to_1()] += 1
		else:
			d_1[item.to_1()] = 0

		if item.to_2() in d_2:
			d_2[item.to_2()] += 1
		else:
			d_2[item.to_2()] = 0

		if item.to_3() in d_3:
			d_3[item.to_3()] += 1
		else:
			d_3[item.to_3()] = 0

		if item.to_4() in d_4:
			d_4[item.to_4()] += 1
		else:
			d_4[item.to_4()] = 0

		if item.to_5() in d_5:
			d_5[item.to_5()] += 1
		else:
			d_5[item.to_5()] = 0

		db.append(item)

print(len(db))
print(len(d_1))
print(len(d_2))
print(len(d_3))
print(len(d_4))
print(len(d_5))

# print("exporting results...")
# with open(f"output/05_02_2023.csv", "w") as f_founds:
# 	print(title, file=f_founds)
# 	for item in tqdm(items):
# 		print(item, file=f_founds)
	