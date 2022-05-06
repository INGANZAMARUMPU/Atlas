from datetime import date, timedelta

last_tot = 0
with open("inputs/06052022.txt") as file:
	f_founds = open("output/06052022_results.txt", "w")
	lines = file.readlines()
	i = 1
	base = date(1800, 1, 1)
	while i < len(lines):
		str_date = f"{base.day}/{base.month}/{base.year}"
		line = str_date+","+",".join(lines[i-1].replace("\n", "").replace("\t", ",").split(";"))
		print(line, file=f_founds)
		base += timedelta(days=1)
		i += 1
	f_founds.close()
