def conta_vogais(palavra):
    VOGAIS = "aeiouAEIOU"
    contador = 0
    
    for letra in palavra:
        if letra in VOGAIS:
            contador +=1

    return contador



palavra = input("Digite uma palavra: ")
resultado = conta_vogais(palavra)

print(f"O número de vogais na string '{palavra}' é: {resultado}")