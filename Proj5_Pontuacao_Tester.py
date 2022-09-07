# Projeto 5
# Desenvolvimento de um código que retorne se
# há ou não alguma pontuação no texto escrito pelo usuário


import string

print(string.punctuation)
frase_inp = input("Escreva uma frase qualquer...")


def contemPontuacao():
    return any(
        ch in string.punctuation
        for ch in frase_inp
    )


print(contemPontuacao())
