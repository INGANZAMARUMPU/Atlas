from datetime import date, timedelta
from tqdm import tqdm

last_tot = 0
with open(f"inputs/date_1.txt") as file:
	lines = file.readline().split("}, {")
	f_founds = open(f"output/combination.txt", "w")
	f_founds_dated = open(f"output/combination_dated.txt", "w")
	base = date(1900, 1, 1)
	for line in tqdm(lines):
	# for line in lines:
		line = line.replace("{","").replace("}","").replace(" ", "")
		str_date = f"{base.day}/{base.month}/{base.year}"

		list_line = line.split(',')
		
		with open(f"inputs/date_2.txt") as second_file:
			second_lines = second_file.readline().split("}, {")
			for second_line in second_lines:
				new_list = None
				
				second_line = second_line.replace("{","").replace("}","").replace(" ", "")
				second_line_list = second_line.split(',')
				
				if(second_line_list[0] == list_line[-1]):
					new_list = list_line + second_line_list[1:]
					result = ",".join(new_list)

					print(result, file=f_founds)
					print(str_date+","+result, file=f_founds_dated)
	f_founds.close()
	f_founds_dated.close()
