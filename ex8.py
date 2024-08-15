# Definindo os conjuntos
A = {1, 2, 3}
C = {1, 2, 3, 4, 5}
D = {5, 3, 4, 2, 1}

# Verificando se A é um subconjunto próprio de C
is_A_proper_subset_of_C = A.issubset(C) and A != C
print(f"A é subconjunto próprio de C: {is_A_proper_subset_of_C}")

# Verificando se D é um subconjunto próprio de C
is_D_proper_subset_of_C = D.issubset(C) and D != C
print(f"D é subconjunto próprio de C: {is_D_proper_subset_of_C}")