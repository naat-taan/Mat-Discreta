A = {1, 2, 3}
C = {1, 2, 3, 4, 5}

is_proper_subset = A.issubset(C) and A != C
print(f"A é subconjunto próprio de C: {is_proper_subset}")