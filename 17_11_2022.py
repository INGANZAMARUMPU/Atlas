import itertools # combinations(list, size) or permutations(list, size)

if __name__ == "__main__":
	print(list(itertools.permutations(["12", "13", "14", "15", "16"], 2)))
