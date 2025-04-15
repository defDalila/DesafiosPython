def elementos_comuns(lista1, lista2):
    # Convert lists to sets and find intersection directly
    return list(set(lista1) & set(lista2))

# Leitura das listas
lista1 = input("Entre com a primeira lista de números inteiros separados por espaços: ").split()
lista2 = input("Entre com a segunda lista de números inteiros separados por espaços: ").split()

# Verifica se todas os elementos das listas podem ser convertidos para inteiros
try:
    # Convert string inputs to integers if possible
    lista1 = list(map(int, lista1))
    lista2 = list(map(int, lista2))
    
    comuns = elementos_comuns(lista1, lista2)
    print(f"Elementos comuns às duas listas: {comuns}")
except ValueError:
    print("Entrada inválida.")
