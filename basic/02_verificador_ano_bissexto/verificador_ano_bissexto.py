def verificador_ano_bissexto():
    ano = int(input("Entre com um ano: "))
    
    regra_um = (ano % 4 == 0) and (ano % 100 != 0)
    regra_dois = ano % 400 == 0
    
    if (regra_um or regra_dois):
        print("SIM")
    else:
        print("NÃO")


verificador_ano_bissexto()
