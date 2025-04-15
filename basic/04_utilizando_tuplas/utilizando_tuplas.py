def soma_tupla(tupla):
    return sum(tupla)

entrada = input("Entre com os números inteiros separados por espaços: ")

elementos = tuple(map(int, entrada.split()))

resultado = soma_tupla(elementos)
print(f"A soma dos elementos da tupla é: {resultado}")