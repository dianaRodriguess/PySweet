import funcoes
import interfaces as ifc
from datetime import datetime
from cruds import produto as pdt
from dicionarios import clientes, produtos, vendas, formas_pagamento


def exibir_venda(id_venda):
    print()
    cliente = clientes[vendas[id_venda][1]][0]
    produto = produtos[vendas[id_venda][0]][0]
    qtd_vendida = vendas[id_venda][2]
    forma_pagamento = formas_pagamento[vendas[id_venda][3]]
    valor_total = vendas[id_venda][4]
    data = vendas[id_venda][5]
    print('‹♥› Informações da Venda ‹♥›')
    print(f"»› Nome do cliente: {cliente}")
    print(f"»› Produto: {produto}")
    print(f"»› Quantidade: {qtd_vendida}")
    print(f"»› Forma de pagamento: {forma_pagamento}")
    print(f"»› Total R$: {valor_total}")
    print(f"»› Data: {data}")
    print("»› ID de cadastro: ", id_venda)
    print()


def valor_venda(id_produto, qtd_vendida):
    preco_produto = float(produtos[id_produto][2])
    qtd_vendida = float(qtd_vendida)
    valor_total = float(qtd_vendida * preco_produto)
    valor_total = f'{valor_total:.2f}'
    return valor_total


def cadastrar_venda():
    ifc.cabecalho_modulos("Cadastrar Venda")
    id_produto = funcoes.ler_codigo("ID do produto: ", produtos)
    id_cliente = funcoes.ler_codigo("ID do cliente: ", clientes)
    qtd_vendida = funcoes.ler_quantidade()
    forma_pagamento = funcoes.ler_form_pag()

    data = datetime.now()
    valor_total = valor_venda(id_produto, qtd_vendida)

    qdt_atual = pdt.atualizar_quantidade(id_produto, int(qtd_vendida))
    produtos[id_produto][1] = qdt_atual

    id_venda = funcoes.gerar_codigo(vendas)
    vendas[id_venda] = [
        id_produto,
        id_cliente,
        qtd_vendida,
        forma_pagamento,
        valor_total,
        data.strftime("%x, %X"),
    ]
    exibir_venda(id_venda)
    print('\033[92m')
    print("»› Venda cadastrada com sucesso!")
    print('\033[0m')
    
    input("»› Tecle <ENTER> para continuar... ")


def pesquisar_venda():
    ifc.cabecalho_modulos("Pesquisar Venda")
    id_venda = funcoes.ler_codigo('Digite o ID de cadastro da venda: ', vendas)
    sair = "n"
    while sair == "n":
        exibir_venda(id_venda)

        sair = input('»› Deseja sair do módulo "Pesquisar Venda" (S/N)? ').lower()
        print()
        if sair == "n":
            id_venda = funcoes.ler_codigo('Digite o ID de cadastro da venda: ', vendas)

    input("»› Tecle <ENTER> para continuar... ")


def atualizar_venda():
    ifc.cabecalho_modulos("Atualizar Venda")
    id_venda = funcoes.ler_codigo('Digite o ID de cadastro da venda: ', vendas)
    sair = 'n'
    while sair == 'n':
        id_produto = funcoes.ler_codigo("ID do produto: ", produtos)
        id_cliente = funcoes.ler_codigo("ID do cliente: ", clientes)
        qtd_vendida = funcoes.ler_quantidade()
        forma_pagamento = funcoes.ler_form_pag()

        data = vendas[id_venda][5]
        valor_total = valor_venda(id_produto, qtd_vendida)

        qdt_atual = pdt.atualizar_quantidade(id_produto, int(qtd_vendida))
        produtos[id_produto][1] = qdt_atual

        id_venda = funcoes.gerar_codigo(vendas)
        vendas[id_venda] = [
            id_produto,
            id_cliente,
            qtd_vendida,
            forma_pagamento,
            valor_total,
            data,
        ]

        print("‹♥› Novos dados da venda ‹♥›")
        exibir_venda(id_venda)
        print('\033[92m')
        print("»› Dados da venda atualizados com sucesso!")
        print('\033[0m')
        
        sair = input('»› Deseja sair do módulo "Atualizar Venda" (S/N)? ').lower()
        print()
        if sair == "n":
            id_venda = funcoes.ler_codigo('Digite o ID de cadastro da venda: ', vendas)
        
    input("»› Tecle <ENTER> para continuar... ")


def deletar_venda():
    ifc.cabecalho_modulos("Deletar Venda")
    id_venda = funcoes.ler_codigo('Digite o ID de cadastro da venda: ', vendas)
    sair = "n"
    while sair == "n":
        exibir_venda(id_venda)
        print('\033[33m')
        resp = input("\n»› Tem certeza que deseja deletar esta venda (S/N)? ").lower()
        print('\033[0m')
        if resp == "s":
            del vendas[id_venda]
            print('\033[92m')
            print("\n»› Venda deletada com sucesso! ")
            print('\033[0m')
        else:
            print('\033[91m')
            print("»› Não foi possível deletar a venda. ")
            print('\033[0m')

        sair = input('»› Deseja sair do módulo "Deletar Venda" (S/N)? ').lower()
        print()
        if sair == "n":
            id_venda = funcoes.ler_codigo('Digite o ID de cadastro da venda: ', vendas)

    input("»› Tecle <ENTER> para continuar... ")
