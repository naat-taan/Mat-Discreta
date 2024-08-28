# Definindo os conjuntos A e B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8, 9, 10}

# a) União de A e B (A ∪ B)
uniao = A | B
print(f"a) A ∪ B = {uniao}")

# b) Interseção de A e B (A ∩ B)
intersecao = A & B
print(f"b) A ∩ B = {intersecao}")

# c) Diferença de A em relação a B (A - B)
diferenca_A_B = A - B
print(f"c) A - B = {diferenca_A_B}")

# d) Diferença de B em relação a A (B - A)
diferenca_B_A = B - A
print(f"d) B - A = {diferenca_B_A}")