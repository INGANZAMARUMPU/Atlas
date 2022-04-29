last_tot = 0
with open("02042022.txt") as file:
	lines = file.readlines()
	groupe1 = []
	groupe2 = []
	f_founds = open("02042022_correct.csv", "w")
	for i, line in enumerate(lines):
		line = line[:-1]
		sol = line.replace(",","")
		if(len(sol) == 9):
			sol = sol[0:3]+" "+sol[3:6]+" "+sol[6:9]
			groupe1.append(f"{i},{line},{sol}")
		else:
			groupe2.append(f"{i},{line}")

	print("sep=,\n", file=f_founds)
	print("\n".join(groupe1), file=f_founds)
	print("\n", file=f_founds)
	print("\n".join(groupe2), file=f_founds)
	f_founds.close()
