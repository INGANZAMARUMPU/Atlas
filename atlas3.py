last_tot = 0
with open("inputs/atlas3.csv") as file:
	lines = file.readlines()
	i = 1
	f_founds = open("atlas3_results.csv", "w")
	
	C1C2C3 = []
	C1C3C4 = []
	C1C4C5 = []
	C2C3C4 = []
	C2C4C5 = []
	C3C4C5 = []
	data = []
	results = []
	
	while i < len(lines):
		line = lines[i].replace("\n", "").split(";")

		C1C2C3.append(line[0]+" "+line[1]+" "+line[2])
		C1C3C4.append(line[0]+" "+line[2]+" "+line[3])
		C1C4C5.append(line[0]+" "+line[3]+" "+line[4])
		C2C3C4.append(line[1]+" "+line[2]+" "+line[3])
		C2C4C5.append(line[1]+" "+line[3]+" "+line[4])
		C3C4C5.append(line[2]+" "+line[3]+" "+line[4])
		new_line = line[0]+" "+line[1]+" "+line[2]+" "+line[3]+" "+line[4]
		data.append(new_line)
		results.append({new_line:[]})
		i+=1
	
	combinaisons = C1C2C3 + C1C3C4 + C1C4C5 + C2C3C4 + C2C4C5 + C3C4C5
	max_length = len(C1C2C3)

	for i, item in enumerate(C1C2C3):
		g_values = [j%max_length for j, x in enumerate(combinaisons) if x == item]
		results[i][data[i]].extend(g_values)

	for i, item in enumerate(C1C3C4):
		g_values = [j%max_length for j, x in enumerate(combinaisons) if x == item]
		results[i][data[i]].extend(g_values)

	for i, item in enumerate(C1C4C5):
		g_values = [j%max_length for j, x in enumerate(combinaisons) if x == item]
		results[i][data[i]].extend(g_values)

	for i, item in enumerate(C2C3C4):
		g_values = [j%max_length for j, x in enumerate(combinaisons) if x == item]
		results[i][data[i]].extend(g_values)

	for i, item in enumerate(C2C4C5):
		g_values = [j%max_length for j, x in enumerate(combinaisons) if x == item]
		results[i][data[i]].extend(g_values)

	for i, item in enumerate(C3C4C5):
		g_values = [j%max_length for j, x in enumerate(combinaisons) if x == item]
		results[i][data[i]].extend(g_values)
	
	print("C1;C2;C3;C4;C5;", file=f_founds)
	i = 1
	for item in results:
		key = list(item.keys())[0]
		cols = ";".join(key.split())
		indexes = list(set(item[key]))[1:]
		values = ""
		for a in indexes:
			values += data[a]+";"
		print(f"{cols};{key};{values}",file=f_founds)
		i+=1


