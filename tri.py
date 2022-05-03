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

with open("inputs/03052022.txt") as file:
	list_line = file.readline().split("}, {")
	f_founds = open("output/03052022.csv", "w")
	combinaisons = []

	for i, line in enumerate(list_line):
		line = line.replace("{","").replace("}","")
		combinaisons.append(Combinaison(i, line))

	combinaisons.sort()
	print("INDEX;C1;C2;C3;C4;C5;COMB;POSITION", file=f_founds)
	for i, combinaison in enumerate(combinaisons):
		print(f"{combinaison};{i}", file=f_founds)


		
		