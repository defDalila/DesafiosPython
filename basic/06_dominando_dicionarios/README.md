#  Dominando Dicionários :dart:

<br>

## :memo: **Descrição** 

O desafio consiste em criar uma função contar_caracteres e adicionar a esta função um dicionário vazio chamado contador para armazenar as contagens de caracteres. Essa função deverá iterar através de cada caractere na string string e para cada caractere, deverá verificar se ele já está presente no dicionário contador. Caso estiver, deverá incrementar o valor associado a essa chave. Caso contrário, a chave deve ser adicionada ao dicionário com valor inicial 1. Neste dicionário, as chaves são os caracteres presentes na string e os valores correspondem à contagem de vezes que cada caractere aparece.

<br/>


## ⌨️ **Entrada**

A função espera receber uma única string como entrada. 

> [!IMPORTANT]
> Neste desafio, consideramos como casos de teste apenas strings textuais.

<br/>

## 🎧 **Saída**

A função retorna um dicionário onde cada chave é um caractere presente na string de entrada e o valor associado a cada chave é a quantidade de vezes que o caractere ocorre na string.

<br/>

## 📲 **Exemplos**

A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 

<br/>

| Entrada     | Saída                                                              |
| ----------- | ------------------------------------------------------------------ |
| collections | `{'c': 2, 'o': 2, 'l': 2, 'e': 1, 't': 1, 'i': 1, 'n': 1, 's': 1}` |
| numpy       | `{'n': 1, 'u': 1, 'm': 1, 'p': 1, 'y': 1}`                         |
| datetime    | `{'d': 1, 'a': 1, 't': 2, 'e': 2, 'i': 1, 'm': 1}`                 |

<br/>

> [!CAUTION]
> As entradas e saídas dos desafios de código devem ser idênticas às definidas na descrição do desafio
