def validar_preco(preco):
    regex_preco = r"([0-9]{1,}(?:\.[0-9]{3})*)[,\.]([0-9]{2})"
    preco = preco.replace(",", ".")
    # if not re.match(regex_preco, preco):
    #    return False
    # return True
    return print(preco)


x = "7,7"
# validar_preco(x)

def ler_preco():
    print()
    preco = input("››››› Preço da Unidade (00,00): ")
    # while not validacoes.validar_preco(preco):
    #     print('\033[91m')
    #     print("»› Ops! Algo deu errado! \n»› Siga o padrão (00,00). Tente novamente...")
    #     print('\033[0m')
        
    #     preco = input("››››› Preço da Unidade (00,00): ")
    preco = preco.replace(",", ".")
    return preco

preco = ler_preco()
print(preco)