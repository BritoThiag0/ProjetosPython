# Projeto 6
# Função para fatoração de um número

#num = int(input("Diga um número: "))

def getFatores(num):
    fatores = []
    divisor = 2
    while (divisor <= num):
        if (num % divisor) == 0:
            fatores.append(divisor)
            num = num//divisor
        else:
            divisor += 1

    print(fatores)
    # return fatores


getFatores(100)
