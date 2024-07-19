import produto as pdt
import interfaces as ifc
from datetime import datetime
from dicionarios import clientes, produtos, formas_pagamento, vendas
from validacoes.validacoes import validarFormaPagamento


def exibir_venda(id_venda):
    cliente = clientes[vendas[id_venda][1]][0]
    produto = produtos[vendas[id_venda][0]][0]
    qtd_vendida = vendas[id_venda][2]
    forma_pagamento = formas_pagamento[vendas[id_venda][3]]
    valor_total = vendas[id_venda][4]
    data = vendas[id_venda][5]
    print()
    print("Venda cadastrado com sucesso!!")
    print()
    print(f"Nome do cliente: {cliente}")
    print(f"Produto: {produto}")
    print(f"Quantidade: {qtd_vendida}")
    print(f"Forma de pagamento: {forma_pagamento}")
    print(f"Total: {valor_total}")
    print(f"Data: {data}")
    print("Id de cadastro: ", id_venda)


def cadastrar_venda():
    ifc.cabecalho_modulos("Cadastrar Venda")
    id_produto = input("##### Produto vendido: ")
    print()
    id_cliente = input("##### Cliente: ")

    if id_produto not in produtos.keys():
        print("Produto não encotrado. ")
    elif id_cliente not in clientes.keys():
        print("Cliente não encontrado. ")
    else:
        print()
        qtd_vendida = input("##### Quantidade vendida: ")
        print()
        valor_total = input("##### Total: ")
        print()
        forma_pagamento = int(
            input(
                "##### Forma de pagamento: \n##### 1 - Cartão de Débito \n##### 2 - Cartão de Crédito \n##### 3 - Espécie \n##### 4 - PIX \n: "
            )
        )

        while not validarFormaPagamento(formas_pagamento, forma_pagamento):
            print("Forma de pagamento invalida. Por favor escola novamente. ")
            forma_pagamento = input(
                "##### Forma de pagamento: \n##### 1 - Cartão de Débito \n##### 2 - Cartão de Crédito \n##### 3 - Espécie \n##### 4 - PIX \n: "
            )

        data = datetime.now()

        qdt_atual = pdt.atualizar_quantidade(id_produto, int(qtd_vendida))
        produtos[id_produto][1] = qdt_atual

        id_venda = vendas.__len__() + 1
        id_venda = str(id_venda)
        vendas[id_venda] = [
            id_produto,
            id_cliente,
            qtd_vendida,
            forma_pagamento,
            valor_total,
            data.strftime("%x, %X"),
        ]
        exibir_venda(id_venda)
        print("Venda cadastrada com sucesso!")
    print()
    input("Tecle <ENTER> para continuar... ")


def pesquisar_venda():
    ifc.cabecalho_modulos("Pesquisar Venda")
    id_venda = input("Qual o id da venda? ")

    if id_venda in vendas.keys():
        print()
        exibir_venda(id_venda)
        print()
    else:
        print("Não foi possível achar a venda. Tem certeza que ela está cadastrada? ")
    print()
    input("Tecle <ENTER> para continuar... ")


def atualizar_venda():
    ifc.cabecalho_modulos("Atualizar Venda")
    id_venda = input("Qual o id da venda? ")
    print()

    if id_venda in vendas.keys():
        id_produto = input("##### Produto vendido: ")
        print()
        id_cliente = input("##### Cliente: ")
        print()
        qtd_vendida = input("##### Quantidade vendida: ")
        print()
        data = input("##### Data (data, hora): ")
        print()
        valor_total = input("##### Total: ")
        forma_pagamento = int(
            input(
                "##### Forma de pagamento: \n##### 1 - Cartão de Débito \n##### 2 - Cartão de Crédito \n##### 3 - Espécie \n##### 4 - PIX \n: "
            )
        )

        while not validarFormaPagamento(formas_pagamento, forma_pagamento):
            print("Forma de pagamento invalida. Por favor escola novamente. ")
            forma_pagamento = input(
                "##### Forma de pagamento: \n##### 1 - Cartão de Débito \n##### 2 - Cartão de Crédito \n##### 3 - Espécie \n##### 4 - PIX \n: "
            )

        if id_produto in produtos.keys():
            if id_cliente in clientes.keys():
                vendas[id_venda] = [
                    id_produto,
                    id_cliente,
                    qtd_vendida,
                    forma_pagamento,
                    valor_total,
                    data,
                ]

                exibir_venda(id_venda)
                print("Dados da venda atualizado com sucesso!")
            else:
                print("Cliente não encontrado. ")
        else:
            print("Produto não encontrado. ")
    else:
        print(
            "Não foi possível encontrar a venda. Tem certeza que ela está cadastrada?"
        )
    print()
    input("Tecle <ENTER> para continuar... ")


def deletar_venda():
    ifc.cabecalho_modulos("Deletar Venda")
    id_venda = input("Qual o id da venda? ")

    if id_venda in vendas.keys():
        print()
        exibir_venda(id_venda)

        resp = input("Tem certeza que deseja excluir esta venda (S/N)? ").lower()

        if resp == "s":
            del vendas[id_venda]
            print("Venda excluida com sucesso! ")
        else:
            print("Não foi possível excluir a venda. ")
    else:
        print("Venda não encontrada. Tem certeza que ela está cadastrada?")
    print()
    input("Tecle <ENTER> para continuar... ")
