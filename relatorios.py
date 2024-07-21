import funcoes 
import interfaces as ifc
from dicionarios import clientes, produtos, vendas


def ver_clientes():
    ifc.interface_ver_clientes()
    for cliente in clientes:
        telefone = clientes[cliente][1]
        tel = f'({telefone[0:2]}) {telefone[2:7]}-{telefone[7:]}'
        endereco = clientes[cliente][3]
        cidade = endereco['cidade']
        rua = endereco['rua']
        bairro = endereco['bairro']
        num_casa = endereco['num_casa']
        logradouro = f'R. {rua} {num_casa}, {bairro}'
        
        logradouro = funcoes.truncate_string(logradouro, 26)
        clientes[cliente][0] = funcoes.truncate_string(clientes[cliente][0], 26)
        clientes[cliente][2] = funcoes.truncate_string(clientes[cliente][2], 26)
        print('| %-8s ' % (cliente), end='')
        print('| %-27s ' % (clientes[cliente][0]), end='')
        print('| %-15s ' % (tel), end='')
        print('| %-26s ' % (clientes[cliente][2]), end='')
        print('| %-29s ' % (logradouro), end='')
        print('| %-22s |' % (cidade))
        print('|══════════|═════════════════════════════|═════════════════|════════════════════════════|═══════════════════════════════|════════════════════════|')
    print()
    input('Tecle <ENTER> para continuar... ')


def ver_vendas():
    ifc.interface_ver_vendas()
    # print(formas_pagamento[vendas['12'][3]])
    # print(vendas)
    for venda in vendas:
        cliente = clientes[vendas[venda][1]][0]
        produto = produtos[vendas[venda][0]][0]
        print('| %-8s ' % (venda), end='')
        print('| %-26s ' % (cliente), end='')
        print('| %-23s ' % (produto), end='')
        print('| %-13s ' % (vendas[venda][2]), end='')
        print('| %-16s ' % (vendas[venda][3]), end='')
        print('| %-10s ' % (vendas[venda][4]), end='')
        print('| %-16s |' % (vendas[venda][5]))

    print(
        '|══════════|════════════════════════════|═════════════════════════|═══════════════|══════════════════|════════════|════════════════════|'
    )
    print()
    input('Tecle <ENTER> para continuar... ')


def ver_produtos():
    ifc.interface_ver_produtos()
    for produto in produtos:
        print('| %-8s ' % (produto), end='')
        print('| %-27s ' % (produtos[produto][0]), end='')
        print('| %-18s ' % (produtos[produto][1]), end='')
        print('| %-15s |' % (produtos[produto][2]))
    print(
        '|══════════|═════════════════════════════|════════════════════|═════════════════|'
    )
    print()
    input('Tecle <ENTER> para continuar... ')


def prdt_mais_vend():
    ifc.interface_prdt_mais_vend()
    produtos_vendidos = {}
    for venda in vendas.values():
        id_produto = venda[0]
        qtd_vendida = int(venda[2])
        if id_produto in produtos_vendidos:
            produtos_vendidos[id_produto] += qtd_vendida
        else:
            produtos_vendidos[id_produto] = qtd_vendida
    lista_quantidade = list(produtos_vendidos.values())
    lista_quantidade.sort(reverse=True)
    for i in range(5):
        for p in produtos_vendidos:
            if produtos_vendidos[p] == lista_quantidade[i]:
                print('| %-27s ' % produtos[p][0], end='')
                print('| %-18s |' % produtos_vendidos[p])
    print('|═════════════════════════════|════════════════════|')
    print()
    input('Tecle <ENTER> para continuar... ')


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
    for i in range(5):
        for c in maiores_compradores:
            if maiores_compradores[c] == lista_quantidade[i]:
                print('| %-27s ' % clientes[c][0], end='')
                print('| %-18s |' % maiores_compradores[c])
    print('|═════════════════════════════|════════════════════|')
    print()
    input('Tecle <ENTER> para continuar... ')
