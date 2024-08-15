C = {2, 3, 4}
subsets = [{2}, {3}, {4}, {2, 3}, {2, 4}, {3, 4}, {2, 3, 4}, set()]

for subset in subsets:
	print(f"{subset} é subconjunto de C: {subset.issubset(C)}")