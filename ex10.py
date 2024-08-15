def obter_conjunto(prompt):
    while True:
        try:
            entrada_usuario = input(prompt)
            return set(entrada_usuario.split())
        except ValueError:
            print("Entrada inválida. Por favor, insira os elementos separados por espaço.")

def exibir_menu():
    print("\nMenu de Operações entre Conjuntos:")
    print("1. União")
    print("2. Intersecção")
    print("3. Diferença (A - B)")
    print("4. Diferença (B - A)")
    print("5. Produto cartesiano")
    print("6. Verificação se A é subconjunto de B")
    print("7. Verificação se B é subconjunto de A")
    print("8. Sair")

def uniao(A, B):
    return A | B

def interseccao(A, B):
    return A & B

def diferenca(A, B):
    return A - B

def diferenca(B, A):
    return B - A

def produto_cartesiano(A, B):
    return {(a, b) for a in A for b in B}

def e_subconjunto(A, B):
    return A <= B

def e_subconjunto_proprio(A, B):
    return A < B

def main():
    A = obter_conjunto("Insira os elementos do conjunto A (separados por espaço): ")
    B = obter_conjunto("Insira os elementos do conjunto B (separados por espaço): ")

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            print("União:", uniao(A, B))
        elif escolha == '2':
            print("Intersecção:", interseccao(A, B))
        elif escolha == '3':
            print("Diferença (A - B):", diferenca(A, B))
        elif escolha == '4':
            print("Diferença (B - A):", diferenca(B, A))
        elif escolha == '5':
            print("Produto cartesiano:", produto_cartesiano(A, B))
        elif escolha == '6':
            print("A é subconjunto de B:", e_subconjunto(A, B))
            print("A é subconjunto próprio de B:", e_subconjunto_proprio(A, B))
        elif escolha == '7':
            print("B é subconjunto de A:", e_subconjunto(B, A))
            print("B é subconjunto próprio de A:", e_subconjunto_proprio(B, A))
        elif escolha == '8':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()