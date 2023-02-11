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
		return f"{self.a},{self.b},{self.c},{self.d},{self.e},{self.c_1},{self.c_2},{self.c_3},{self.c_4},{self.c_5}"

d_1 = dict()
d_2 = dict()
d_3 = dict()
d_4 = dict()
d_5 = dict()
items = []

title = "A,B,C,D,E,A COUNT,AB COUNT,ABC COUNT,ABCD COUNT,ABCDE COUNT"

print("reading sources...")
with open(f"inputs/05_02_2023.csv") as file:
	file.readline()
	for line in tqdm(file.readlines()):
		item = Item(*[x for x in line[:-1].split(",") if x != ''])

		if item.to_1() in d_1:
			d_1[item.to_1()] += 1
		else:
			d_1[item.to_1()] = 1

		if item.to_2() in d_2:
			d_2[item.to_2()] += 1
		else:
			d_2[item.to_2()] = 1

		if item.to_3() in d_3:
			d_3[item.to_3()] += 1
		else:
			d_3[item.to_3()] = 1

		if item.to_4() in d_4:
			d_4[item.to_4()] += 1
		else:
			d_4[item.to_4()] = 1

		if item.to_5() in d_5:
			d_5[item.to_5()] += 1
		else:
			d_5[item.to_5()] = 1

		items.append(item)

print("exporting results...")
with open(f"output/05_02_2023.csv", "w") as f_founds:
	print(title, file=f_founds)
	c_c_1 = 0
	c_c_2 = 0
	c_c_3 = 0
	c_c_4 = 0
	c_c_5 = 0
	for item in tqdm(items):
		item.c_1 = d_1[item.to_1()] - c_c_1
		item.c_2 = d_2[item.to_2()] - c_c_2
		item.c_3 = d_3[item.to_3()] - c_c_3
		item.c_4 = d_4[item.to_4()] - c_c_4
		item.c_5 = d_5[item.to_5()] - c_c_5
		c_c_1 += 1
		c_c_2 += 1
		c_c_3 += 1
		c_c_4 += 1
		c_c_5 += 1
		
		if(c_c_1 == d_1[item.to_1()]):
			c_c_1 = 0

		if(c_c_2 == d_2[item.to_2()]):
			c_c_2 = 0

		if(c_c_3 == d_3[item.to_3()]):
			c_c_3 = 0

		if(c_c_4 == d_4[item.to_4()]):
			c_c_4 = 0

		if(c_c_5 == d_5[item.to_5()]):
			c_c_5 = 0

		print(item, file=f_founds)
	