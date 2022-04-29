last_tot = 0
with open("atlas2.csv") as file:
	lines = file.readlines()
	i = 1
	f_founds = open("groupes_founds.csv", "w")
	while i < len(lines):
		tot = lines[i].replace("\n", "").split(";")[-1]
		count = 1
		j = i+count
		print(j)
		while int(tot) == int(lines[j].split(";")[-1]):
			count += 1
			j = i+count
		k = 0
		while k < count:
			if k == 0:
				new_line = lines[i+k].replace("\n","")+f";{count}"
			else:
				new_line = lines[i+k].replace("\n","")
			k += 1
			print(new_line, file=f_founds)
		i += count

