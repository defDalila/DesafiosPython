def contar_caracteres(palavra):
    contador = dict()
    
    for letra in palavra:
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1
        
    return contador

entrada = input("Insira uma palavra: ").lower().strip()

resultado = contar_caracteres(entrada)

print(resultado)