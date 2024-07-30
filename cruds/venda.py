import funcoes
import interfaces as ifc
from datetime import datetime
from cruds import produto as pdt
from dicionarios import clientes, produtos, vendas, formas_pagamento


def exibir_venda(id_venda):
    print()
    cliente = clientes[vendas[id_venda][1]][0]
    produto_vendidos = vendas[id_venda][0]
    qtd_vendida = vendas[id_venda][2]
    forma_pagamento = formas_pagamento[vendas[id_venda][3]]
    valor_total = f"{float(vendas[id_venda][4]):.2f}"
    data = vendas[id_venda][5]
    print('‹♥› Informações da Venda ‹♥›')
    print("-------------------------------------------------------------------------------")
    print('    ID    |           Produto           |     Quantidade     |    Preço (R$)   ')
    print("-------------------------------------------------------------------------------")
    for key, value in produto_vendidos.items():
        nome_produto = funcoes.truncate_string(produtos[key][0], 26)
        quantidade = value[0]
        preco = value[1]
        print(' %-8s |' % (key), end='')
        print(' %-27s |' % (nome_produto), end='')
        print(' %-18s |' % (quantidade), end='')
        print(' %-15s ' % (preco))
    print("-------------------------------------------------------------------------------")
    print(f"\n»› Nome do cliente: {cliente}")
    print(f"»› Itens Totais: {qtd_vendida}")
    print(f"»› Forma de pagamento: {forma_pagamento}")
    print(f"»› Valor Total R$: {valor_total}")
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
    produtos_vendidos = {}
    sair_1 = 'n'
    while sair_1 == 'n':
        nome_produto = input('Digite o nome do produto: ')
        while not funcoes.nome_indicio(nome_produto, produtos):
            print('\033[91m')
            print("»› Ops! Algo deu errado! \n»› Tem certeza que este é código certo? Tente novamente...")
            print('\033[0m')
            nome_produto = input('\nDigite o nome do produto: ')
        id_produto = funcoes.nome_pra_codigo(nome_produto, produtos)  # Recebe ID do produto
        qtd_vend_produto = funcoes.ler_quantidade()  # Ler quantidade vendida do produo
        
        qdt_atual = pdt.atualizar_quantidade(id_produto, int(qtd_vend_produto))  # Atualiza a quantidade no dicionario
        produtos[id_produto][1] = qdt_atual
        valor_produto = valor_venda(id_produto, qtd_vend_produto)  # Calcula o valor do produto (preço * qtd_vend_produto)
        
        produtos_vendidos[id_produto] = [qtd_vend_produto, valor_produto] 
        
        sair_1 = input('SAIR (S/N): ').lower()  # Controle
        # id_produto = funcoes.ler_codigo("ID do produto: ", produtos)  # Ler ID do produto
        
        if sair_1 == 'n':
            nome_produto = input('Digite o nome do produto: ')
            while not funcoes.nome_indicio(nome_produto, produtos):
                print('\033[91m')
                print("»› Ops! Algo deu errado! \n»› Tem certeza que este é nome certo? Tente novamente...")
                print('\033[0m')
                nome_produto = input('\nDigite o nome do produto: ')
            id_produto = funcoes.nome_pra_codigo(nome_produto, produtos)
            qtd_vend_produto = funcoes.ler_quantidade()
            
            qdt_atual = pdt.atualizar_quantidade(id_produto, int(qtd_vend_produto))
            produtos[id_produto][1] = qdt_atual
            valor_produto = valor_venda(id_produto, qtd_vend_produto)
            
            produtos_vendidos[id_produto] = [qtd_vend_produto, valor_produto]
            
            sair_1 = input('SAIR (S/N): ').lower()
    
    id_cliente = funcoes.ler_codigo("ID do cliente: ", clientes) 
    forma_pagamento = funcoes.ler_form_pag()
    
    # Calcula o total da quantidade vendida e do valor
    qtd_vendida = 0
    valor_total = 0
    for items in produtos_vendidos.values():
        qtd_vendida += int(items[0])
        valor_total += float(items[1])
        

    data = datetime.now()

    id_venda = funcoes.gerar_codigo(vendas)
    vendas[id_venda] = [
        produtos_vendidos,
        id_cliente,
        str(qtd_vendida),
        forma_pagamento,
        str(valor_total),
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
        produtos_vendidos = {}
        sair_1 = 'n'
        while sair_1 == 'n':
            id_produto = funcoes.ler_codigo("ID do produto: ", produtos)  # Ler ID do produto
            qtd_vend_produto = funcoes.ler_quantidade()  # Ler quantidade vendida do produo
            
            qdt_atual = pdt.atualizar_quantidade(id_produto, int(qtd_vend_produto))  # Atualiza a quantidade no dicionario
            produtos[id_produto][1] = qdt_atual
            valor_produto = valor_venda(id_produto, qtd_vend_produto)  # Calcula o valor do produto (preço * qtd_vend_produto)
            
            produtos_vendidos[id_produto] = [qtd_vend_produto, valor_produto] 
            
            sair_1 = input('SAIR (S/N): ').lower()  # Controle
            
            if sair_1 == 'n':
                id_produto = funcoes.ler_codigo("ID do produto: ", produtos)
                qtd_vend_produto = funcoes.ler_quantidade()
                
                qdt_atual = pdt.atualizar_quantidade(id_produto, int(qtd_vend_produto))
                produtos[id_produto][1] = qdt_atual
                valor_produto = valor_venda(id_produto, qtd_vend_produto)
                
                produtos_vendidos[id_produto] = [qtd_vend_produto, valor_produto]
                
                sair_1 = input('SAIR (S/N): ').lower()
    
        id_cliente = funcoes.ler_codigo("ID do cliente: ", clientes) 
        forma_pagamento = funcoes.ler_form_pag()
            
        # Calcula o total da quantidade vendida e do valor
        qtd_vendida = 0
        valor_total = 0
        for items in produtos_vendidos.values():
            qtd_vendida += int(items[0])
            valor_total += float(items[1])
        
        data = vendas[id_venda][5]

        vendas[id_venda] = [
            produtos_vendidos,
            id_cliente,
            str(qtd_vendida),
            forma_pagamento,
            str(valor_total),
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
