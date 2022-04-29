last_tot = 0
with open("atlas3.csv") as file:
	lines = file.readlines()
	i = 1
	f_founds = open("atlas3_results.csv", "w")
	
	C1C2C3 = []
	C1C3C4 = []
	C1C4C5 = []
	C2C3C4 = []
	C2C4C5 = []
	C3C4C5 = []
	
	while i < len(lines):
		line = lines[i].replace("\n", "").split(";")

		C1C2C3.append({
			"key": line[0]+" "+line[1]+" "+line[2],
			"remain": line[3]+" "+line[4],
		})
		C1C3C4.append({
			"key": line[0]+" "+line[2]+" "+line[3],
			"remain": line[1]+" "+line[4],
		})
		C1C4C5.append({
			"key": line[0]+" "+line[3]+" "+line[4],
			"remain": line[1]+" "+line[2],
		})
		C2C3C4.append({
			"key": line[1]+" "+line[2]+" "+line[3],
			"remain": line[0]+" "+line[4],
		})
		C2C4C5.append({
			"key": line[1]+" "+line[3]+" "+line[4],
			"remain": line[0]+" "+line[2],
		})
		C3C4C5.append({
			"key": line[2]+" "+line[3]+" "+line[4],
			"remain": line[0]+" "+line[1],
		})
		i+=1

	for i, item in enumerate(C1C2C3):
		l_count = len([x for x in C1C2C3 if x["key"] == item["key"]])
		g_count = len([x for x in C1C2C3 + C1C3C4 + C1C4C5 + C2C3C4 + C2C4C5 + C3C4C5 if x["key"] == item["key"]])
		C1C2C3[i]["l_value"] = l_count
		C1C2C3[i]["g_value"] = g_count
		C1C2C3[i]["remain"] = item["remain"]

	for i, item in enumerate(C1C3C4):
		l_count = len([x for x in C1C3C4 if x["key"] == item["key"]])
		g_count = len([x for x in C1C2C3 + C1C3C4 + C1C4C5 + C2C3C4 + C2C4C5 + C3C4C5 if x["key"] == item["key"]])
		C1C3C4[i]["l_value"] = l_count
		C1C3C4[i]["g_value"] = g_count
		C1C3C4[i]["remain"] = item["remain"]

	for i, item in enumerate(C1C4C5):
		l_count = len([x for x in C1C4C5 if x["key"] == item["key"]])
		g_count = len([x for x in C1C2C3 + C1C3C4 + C1C4C5 + C2C3C4 + C2C4C5 + C3C4C5 if x["key"] == item["key"]])
		C1C4C5[i]["l_value"] = l_count
		C1C4C5[i]["g_value"] = g_count
		C1C4C5[i]["remain"] = item["remain"]

	for i, item in enumerate(C2C3C4):
		l_count = len([x for x in C2C3C4 if x["key"] == item["key"]])
		g_count = len([x for x in C1C2C3 + C1C3C4 + C1C4C5 + C2C3C4 + C2C4C5 + C3C4C5 if x["key"] == item["key"]])
		C2C3C4[i]["l_value"] = l_count
		C2C3C4[i]["g_value"] = g_count
		C2C3C4[i]["remain"] = item["remain"]

	for i, item in enumerate(C2C4C5):
		l_count = len([x for x in C2C4C5 if x["key"] == item["key"]])
		g_count = len([x for x in C1C2C3 + C1C3C4 + C1C4C5 + C2C3C4 + C2C4C5 + C3C4C5 if x["key"] == item["key"]])
		C2C4C5[i]["l_value"] = l_count
		C2C4C5[i]["g_value"] = g_count
		C2C4C5[i]["remain"] = item["remain"]

	for i, item in enumerate(C3C4C5):
		l_count = len([x for x in C3C4C5 if x["key"] == item["key"]])
		g_count = len([x for x in C1C2C3 + C1C3C4 + C1C4C5 + C2C3C4 + C2C4C5 + C3C4C5 if x["key"] == item["key"]])
		C3C4C5[i]["l_value"] = l_count
		C3C4C5[i]["g_value"] = g_count
		C3C4C5[i]["remain"] = item["remain"]
	
	
	print("C1;C2;C3;C4;C5;C1+C2+C3;local;global;remain;;C1+C3+C4;local;global;remain;;C1+C4+C5;local;global;remain;;C2+C3+C4;local;global;remain;;C2+C4+C5;local;global;remain;;C3+C4+C5;local;global;remain;;", file=f_founds)
	i = 1
	while i < len(lines):
		line = lines[i].replace("\n", "").split(";")
		print(f"{line[0]};{line[1]};{line[2]};{line[3]};{line[4]};\
			{C1C2C3[i-1]['key']};{C1C2C3[i-1]['l_value']};{C1C2C3[i-1]['g_value']};{C1C2C3[i-1]['remain']};;\
			{C1C3C4[i-1]['key']};{C1C3C4[i-1]['l_value']};{C1C3C4[i-1]['g_value']};{C1C3C4[i-1]['remain']};;\
			{C1C4C5[i-1]['key']};{C1C4C5[i-1]['l_value']};{C1C4C5[i-1]['g_value']};{C1C4C5[i-1]['remain']};;\
			{C2C3C4[i-1]['key']};{C2C3C4[i-1]['l_value']};{C2C3C4[i-1]['g_value']};{C2C3C4[i-1]['remain']};;\
			{C2C4C5[i-1]['key']};{C2C4C5[i-1]['l_value']};{C2C4C5[i-1]['g_value']};{C2C4C5[i-1]['remain']};;\
			{C3C4C5[i-1]['key']};{C3C4C5[i-1]['l_value']};{C3C4C5[i-1]['g_value']};{C3C4C5[i-1]['remain']};;",\
		file=f_founds)
		i+=1


