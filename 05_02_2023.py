from dataclasses import dataclass, field
from tqdm import tqdm

@dataclass(order=True)
class Item:
	a:int
	b:int
	c:int
	d:int
	e:int

	c_a:int = field(init=False, default=0)
	c_ab:int = field(init=False, default=0)
	c_abc:int = field(init=False, default=0)
	c_abcd:int = field(init=False, default=0)
	c_abcde:int = field(init=False, default=0)

	def to_1():
		return f"{self.a}"
	def to_2():
		return f"{self.a}_{self.b}"
	def to_3():
		return f"{self.a}_{self.b}_{self.c}"
	def to_4():
		return f"{self.a}_{self.b}_{self.c}_{self.d}"
	def to_5():
		return f"{self.a}_{self.b}_{self.c}_{self.d}_{self.e}"

	def __str__(self):
		return f"{self.a};{self.b};{self.c};{self.d};{self.e};{self.c_a};{self.c_ab};{self.c_abc};{self.c_abcd};{self.c_abcde}"

c_1 = dict()
c_2 = dict()
c_3 = dict()
c_4 = dict()
c_5 = dict()
db = []

title = "A;B;C;D;E;A,AB,ABC,ABCD,ABCDE"

print("reading sources...")
with open(f"inputs/05_02_2023.csv") as file:
	file.readline()
	for line in tqdm(file.readlines()):
		item = Item(*[x for x in line[:-1].split(",") if x != ''])
		db.append(item)

print(len(db))
# print("exporting results...")
# with open(f"output/05_02_2023.csv", "w") as f_founds:
# 	print(title, file=f_founds)
# 	for item in tqdm(items):
# 		print(item, file=f_founds)
	