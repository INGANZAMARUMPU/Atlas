from datetime import date, timedelta

last_tot = 0
for a in [1, 2]:
	with open(f"inputs/date_{a}.txt") as file:
		list_line = file.readline().split("}, {")
		f_founds = open(f"output/date_{a}.txt", "w")
		base = date(1900, 1, 1)
		for i, line in enumerate(list_line):
			line = line.replace("{","").replace("}","")
			str_date = f"{base.day}/{base.month}/{base.year}"
			line = str_date+","+line
			# print("{" + line.replace(" ", "") + "}", file=f_founds, end="")
			print(line.replace(" ", ""), file=f_founds)
			base += timedelta(days=1)
		f_founds.close()
