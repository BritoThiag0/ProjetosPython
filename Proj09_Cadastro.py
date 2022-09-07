# Projeto 9
# Cadastro de pessoas

def cadastro():
    lista = []
    ent = ""
    while ent != "Pare":
        ent = input(
            "Informe o nome para cadastro. \n(Caso deseje encerrar o cadastro, escreva Pare)\n\t")
        if ent == "Pare":
            break
        lista.append(ent)
    return lista


print(cadastro())
