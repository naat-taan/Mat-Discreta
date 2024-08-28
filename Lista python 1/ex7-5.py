C = {1, 2, 3, 4, 5}
D = {5, 3, 4, 2, 1}

is_proper_subset = D.issubset(C) and D != C
print(f"D é subconjunto próprio de C: {is_proper_subset}")