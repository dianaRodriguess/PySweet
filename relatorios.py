import os
import funcoes 
import interfaces as ifc
from dicionarios import clientes, produtos, vendas


def ver_clientes():
    ifc.interface_ver_clientes()
    for cliente in clientes:
        telefone = clientes[cliente][1]
        tel = f'({telefone[0:2]}) {telefone[2:7]}-{telefone[7:]}'
        endereco = clientes[cliente][3]
        rua = endereco['rua']
        bairro = endereco['bairro']
        num_casa = endereco['num_casa']
        
        cidade = funcoes.truncate_string(endereco['cidade'], 22)
        logradouro = funcoes.truncate_string(f'R. {rua} {num_casa}, {bairro}', 27)
        nome_cliente = funcoes.truncate_string(clientes[cliente][0], 26)
        email_cliente = funcoes.truncate_string(clientes[cliente][2], 26)
        
        print('| %-8s ' % (cliente), end='')
        print('| %-27s ' % (nome_cliente), end='')
        print('| %-15s ' % (tel), end='')
        print('| %-26s ' % (email_cliente), end='')
        print('| %-29s ' % (logradouro), end='')
        print('| %-22s |' % (cidade))
        print('|══════════|═════════════════════════════|═════════════════|════════════════════════════|═══════════════════════════════|════════════════════════|')
    print()
    input('»› Tecle <ENTER> para continuar... ')


def ver_vendas():
    ifc.interface_ver_vendas()
    # print(vendas)
    # produto = funcoes.truncate_string(produtos[vendas[venda][0]][0], 23)
    for venda in vendas:
        print('|══════════|════════════════════════════|════════════════|══════════════════|═══════════════|════════════════════|')
        print('|    ID    |          Comprador         |  Total Itens   |  Form.Pagamento  |  Valor Total  |        Data        |')
        print('|══════════|════════════════════════════|════════════════|══════════════════|═══════════════|════════════════════|')
        cliente = funcoes.truncate_string(clientes[vendas[venda][1]][0], 26)
        produtos_vend = vendas[venda][0]
        valor = f"RS$ {float(vendas[venda][4]):.2f}"
        # valor = f'{valor:.2f}'
        print('| %-8s ' % (venda), end='')
        print('| %-26s ' % (cliente), end='')
        print('| %-14s ' % (vendas[venda][2]), end='')
        print('| %-16s ' % (vendas[venda][3]), end='')
        print('| %-13s ' % (valor), end='')
        print('| %-16s |' % (vendas[venda][5]))
        # print('| %-23s ' % (vendas[venda][0]), end='')
        print('|════════════════════════════════════════════════════════════════════════════════════════════════════════════════|')
        print('\33[92m')
        ifc.interface_prdt_vend(venda)
        for prod, detalhes in produtos_vend.items(): 
            quant = detalhes[0]
            prec = 'RS$ ' + detalhes[1]
            nome_produto = funcoes.truncate_string(produtos[prod][0], 35)
            print('| %-17s ' % (prod), end='')
            print('| %-36s ' % (nome_produto), end='')
            print('| %-15s ' % (quant), end='')
            print('| %-33s |' % (prec))
            print('|════════════════════════════════════════════════════════════════════════════════════════════════════════════════|')
        print('\33[0m')
    print('|════════════════════════════════════════════════════════════════════════════════════════════════════════════════|')
    print()
    input('»› Tecle <ENTER> para continuar... ')


def ver_produtos():
    ifc.interface_ver_produtos()
    for produto in produtos:
        nome_produto = funcoes.truncate_string(produtos[produto][0], 26)
        print('| %-8s ' % (produto), end='')
        print('| %-27s ' % (nome_produto), end='')
        print('| %-18s ' % (produtos[produto][1]), end='')
        print('| %-15s |' % (produtos[produto][2]))
    print(
        '|══════════|═════════════════════════════|════════════════════|═════════════════|'
    )
    print()
    input('»› Tecle <ENTER> para continuar... ')


def prdt_mais_vend():
    ifc.interface_prdt_mais_vend()
    produtos_mais_vendidos = {}
    produtos_vendidos = {}
    for venda in vendas.values():
        produtos_vendidos = venda[0]
        for produto, detalhes in produtos_vendidos.items():
            
            id_produto = produto
            qtd_vendida = int(detalhes[0])
        if id_produto in produtos_mais_vendidos:
            produtos_mais_vendidos[id_produto] += qtd_vendida
        else:
            produtos_mais_vendidos[id_produto] = qtd_vendida
    lista_quantidade = list(produtos_mais_vendidos.values())
    lista_quantidade.sort(reverse=True)
    
    try:
        for i in range(5):
            for p in produtos_mais_vendidos:
                if produtos_mais_vendidos[p] == lista_quantidade[i]:
                    nome_produto = funcoes.truncate_string(produtos[p][0], 27)
                    print('| %-27s ' % nome_produto, end='')
                    print('| %-18s |' % produtos_mais_vendidos[p])
        print('|═════════════════════════════|════════════════════|')
    except IndexError:
        print('|═════════════════════════════|════════════════════|')
        
        print('\033[93m')
        print('\n»› Ops! Não é possível mostrar os cinco produtos que mais vendem. \n»› Não há vendas o suficiente.')
        print('\033[0m')
    print()
    input('»› Tecle <ENTER> para continuar... ')


def maiores_compradores():
    ifc.interface_maiores_compradores()
    maiores_compradores = {}
    for venda in vendas.values():
        id_cliente = venda[1]
        qtd_vendida = int(venda[2])
        if id_cliente in maiores_compradores:
            maiores_compradores[id_cliente] += qtd_vendida
        else:
            maiores_compradores[id_cliente] = qtd_vendida
    lista_quantidade = list(maiores_compradores.values())
    lista_quantidade.sort(reverse=True)
    try:
        for i in range(5):
            for c in maiores_compradores:
                if maiores_compradores[c] == lista_quantidade[i]:
                    nome_cliente = funcoes.truncate_string(clientes[c][0], 27)
                    print('| %-27s ' % nome_cliente, end='')
                    print('| %-18s |' % maiores_compradores[c])
        print('|═════════════════════════════|════════════════════|')
    except IndexError:
        print('|═════════════════════════════|════════════════════|')
        print('\033[93m')
        print('\n»› Ops! Não é possível mostrar os cinco maiores compradores. \n»› Não há vendas o suficiente.')
        print('\033[0m')
    print()
    input('»› Tecle <ENTER> para continuar... ')


def checar_estoque():
    os.system('clear')
    estoque_baixo = []
    estoque_critico = []
    # estoque_ok = []
    for value in produtos.values():
        quantidade = int(value[1])
        nome = value[0]
        if quantidade <= 10 and quantidade > 0:
            estoque_baixo.append((nome, quantidade))
        elif quantidade <= 0:
            estoque_critico.append((nome, quantidade))
        else:
            pass
            # estoque_ok.append((nome, quantidade))
    if estoque_baixo:
        print('\033[93m', end='')
        print("-------------------------------------------------------------------------------")
        print('O ESTOQUE DESSES PRODUTOS ESTÁ BAIXO')
        print("-------------------------------------------------------------------------------")
        for nome, quantidade in estoque_baixo:
            print('%-50s |' % nome, end='')
            print(' %-10s ' % quantidade)
        print('\033[0m')
        
    if estoque_critico:
        print('\033[91m', end='')
        print("-------------------------------------------------------------------------------")
        print('O ESTOQUE DESSES PRODUTOS ESTÁ CRITICAMENTE BAIXO')
        print("-------------------------------------------------------------------------------")
        print()
        for nome, quantidade in estoque_critico:
            print('%-50s |' % nome, end='')
            print(' %-10s ' % quantidade)
        print('\033[0m')
        
    if not estoque_baixo and not estoque_critico:
        print('\033[92m', end='')
        print("-------------------------------------------------------------------------------")
        print('NENHUM PRODUTO ESTÁ COM O ESTOQUE BAIXO OU CRÍTICO')
        print("-------------------------------------------------------------------------------")
        print('\033[0m')
    input("»› Tecle <ENTER> para continuar... ")   
