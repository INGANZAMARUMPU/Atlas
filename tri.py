class Combinaison:
	def __init__(self, index, line):
		self.index = index
		self.line = line.replace(" ","").replace(",", ";").replace("\n", "")
		self.value = self.line.replace(";","")

	def __lt__(self, other):
		return int(self.value) < int(other.value)

	def __eq__(self, other):
		return int(self.value) == int(other.value)

	def __str__(self):
		return f"{self.index};{self.line};{self.value}"

	@property
	def is_nined(self):
		return len(self.value) == 9

with open("inputs/03052022.txt") as file:
	list_line = file.readline().split("}, {")
	f_founds = open("output/03052022.csv", "w")
	combinaisons_9 = []
	combinaisons_0 = []

	comb:Combinaison = None
	for i, line in enumerate(list_line):
		line = line.replace("{","").replace("}","")
		comb = Combinaison(i, line)
		combinaisons_9.append(comb) if comb.is_nined else combinaisons_0.append(comb)

	combinaisons_9.sort()
	combinaisons_0.sort()
	print("INDEX;C1;C2;C3;C4;C5;COMB;POSITION", file=f_founds)
	for i, combinaison in enumerate(combinaisons_9):
		print(f"{combinaison};{i}", file=f_founds)

	print("\n", file=f_founds)
	for i, combinaison in enumerate(combinaisons_0):
		print(f"{combinaison};{i}", file=f_founds)


		
		