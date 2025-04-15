from collections import Counter

def contar_caracteres(palavra):
    # Use Counter to count occurrences of each character
    return Counter(palavra)

entrada = input("Insira uma palavra: ").lower().strip()
resultado = contar_caracteres(entrada)
print(resultado)