import funcoes
import interfaces as ifc
from dicionarios import produtos


def exibir_produto(id_produto):
    print()
    produto = produtos[id_produto][0]
    quantidade = produtos[id_produto][1]
    preco = produtos[id_produto][2]
    print('‹♥› Informações do Produto ‹♥›')
    print(f"»› Nome do produto: {produto}")
    print(f"»› Quantidade: {quantidade}")
    print(f"»› Preço da Unidade: R$ {preco}")
    print("»› ID de cadastro: ", id_produto)
    print()


def atualizar_quantidade(id_produto, qtd_vendida):
    qtd_produto = int(produtos[id_produto][1])
    qtd_atual = qtd_produto - qtd_vendida
    return qtd_atual


def cadastrar_produto():
    ifc.cabecalho_modulos("Cadastrar Produto")
    nome_produto = funcoes.ler_nome()
    qtd_produto = funcoes.ler_quantidade()
    preco_produto = funcoes.ler_preco()

    id_produto = funcoes.gerar_codigo(produtos)
    produtos[id_produto] = [nome_produto, qtd_produto, preco_produto]

    print()
    exibir_produto(id_produto)
    print('\033[92m')
    print("»› Produto cadastrado com sucesso!!")
    print('\033[0m')

    input("»› Tecle <ENTER> para continuar... ")


def pesquisar_produto():
    ifc.cabecalho_modulos("Pesquisar Produto")
    nome_prod = input('Digite o nome do produto: ').lower()
    lista_nomes = []
    
    for codigo in produtos:
        nome_produto = produtos[codigo][0].lower()
        # print(nome_produto)
        if nome_prod in nome_produto:
            lista_nomes.append(nome_produto)
    # print(lista_nomes)
    if not lista_nomes:
        print('\nNÃO HÁ PRODUTOS COM ESSE NOME\n')
    else:
        ifc.interface_pesquisar_produtos()
        for nome in lista_nomes:
            for p in produtos:
                if nome.lower() == produtos[p][0].lower():
                    nome_produto = funcoes.truncate_string(produtos[p][0], 26)
                    print('| %-8s ' % (p), end='')
                    print('| %-27s ' % (nome_produto), end='')
                    print('| %-18s ' % (produtos[p][1]), end='')
                    print('| %-15s |' % (produtos[p][2]))
            print('|══════════|═════════════════════════════|════════════════════|═════════════════|')
        detalhe = input('\n»› Quer informações detalhadas de um produto (S/N)? ').lower()
        if detalhe == 's':
            id_produto = funcoes.ler_codigo('Digite o ID de cadastro do produto: ', produtos)
            exibir_produto(id_produto)
        
    input("»› Tecle <ENTER> para continuar... ")


def atualizar_produto():
    ifc.cabecalho_modulos("Atualizar Produto")
    id_produto = funcoes.ler_codigo('Digite o ID de cadastro do produto: ', produtos)
    sair = 'n'
    while sair == 'n':
        nome_produto = funcoes.ler_nome()
        qtd_produto = funcoes.ler_quantidade()
        preco_produto = funcoes.ler_preco()

        produtos[id_produto] = [nome_produto, qtd_produto, preco_produto]
        
        print("‹♥› Novos dados do produto ‹♥›")
        exibir_produto(id_produto)
        print('\033[92m')
        print("»› Dados do produto atualizados com sucesso!")
        print('\033[0m')
        
        sair = input('»› Deseja sair do módulo "Atualizar Produto" (S/N)? ').lower()
        print()
        if sair == "n":
            id_produto = funcoes.ler_codigo('Digite o ID de cadastro do produto: ', produtos)

    input("»› Tecle <ENTER> para continuar... ")


def deletar_produto():
    ifc.cabecalho_modulos("Deletar Produto")
    id_produto = funcoes.ler_codigo('Digite o ID de cadastro do produto: ', produtos)
    sair = 'n'
    while sair == 'n':
        exibir_produto(id_produto)
        print('\033[33m')
        resp = input("\n»› Tem certeza que deseja deletar este produto (S/N)? ").lower()
        print('\033[0m')
        if resp == "s":
            del produtos[id_produto]
            print('\033[92m')
            print("\n»› Produto deletado com sucesso! ")
            print('\033[0m')
        else:
            print('\033[91m')
            print("\n»› Não foi possível deletar o produto. ")
            print('\033[0m')
            
        sair = input('»› Deseja sair do módulo "Deletar Produto" (S/N)? ').lower()
        print()
        if sair == "n":
            id_produto = funcoes.ler_codigo('Digite o ID de cadastro do produto: ', produtos)

    input("»› Tecle <ENTER> para continuar... ")
