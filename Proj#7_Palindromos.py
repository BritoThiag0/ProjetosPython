# Projeto 7
# Verifica se uma string é um palíndromo ou não
# Palíndromo = Uma palavra/frase que é igual de trás pra frente

import re


def ePalindromo(frase):
    normal = ''.join(re.findall(r'[a-z]+', frase.lower()))
    inverso = normal[:: -1]
    # return normal == inverso
    print(normal == inverso)


ePalindromo('Ana')
