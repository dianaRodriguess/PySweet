import interfaces as ifc
from dicionarios import produtos
import funcoes


def exibir_produto(id_produto):
    print()
    produto = produtos[id_produto][0]
    quantidade = produtos[id_produto][1]
    preco = produtos[id_produto][2]
    print('»› Informações do Produto ‹«')
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
    print("\n»› Produto cadastrado com sucesso!!")
    print()
    input("»› Tecle <ENTER> para continuar... ")


def pesquisar_produto():
    ifc.cabecalho_modulos("Pesquisar Produto")
    id_produto = funcoes.ler_codigo('Digite o ID de cadastro do produto: ', produtos)
    sair = 'n'
    while sair == 'n':
        if id_produto in produtos.keys():
            exibir_produto(id_produto)
        else:
            print("\n»› Não foi possível achar o produto. Tem certeza que ele está cadastrado? ")
        
        sair = input('\n»› Deseja sair do módulo "Pesquisar Produto" (S/N)? ').lower()
        print()
        if sair == "n":
            id_produto = funcoes.ler_codigo('Digite o ID de cadastro do produto: ', produtos)

    print()
    input("»› Tecle <ENTER> para continuar... ")


def atualizar_produto():
    ifc.cabecalho_modulos("Atualizar Produto")
    id_produto = funcoes.ler_codigo('Digite o ID de cadastro do produto: ', produtos)
    sair = 'n'
    while sair == 'n':
        if id_produto in produtos.keys():
            nome_produto = funcoes.ler_nome()
            qtd_produto = funcoes.ler_quantidade()
            preco_produto = funcoes.ler_preco()

            produtos[id_produto] = [nome_produto, qtd_produto, preco_produto]

            print()
            exibir_produto(id_produto)
            print()
        else:
            print("\n»› Não foi possível encontrar o produto. Tem certeza que ele está cadastrado?")
            
        sair = input('\n»› Deseja sair do módulo "Atualizar Produto" (S/N)? ').lower()
        print()
        if sair == "n":
            id_produto = funcoes.ler_codigo('Digite o ID de cadastro do produto: ', produtos)
    print()
    input("»› Tecle <ENTER> para continuar... ")


def deletar_produto():
    ifc.cabecalho_modulos("Deletar Produto")
    id_produto = funcoes.ler_codigo('Digite o ID de cadastro do produto: ', produtos)
    sair = 'n'
    while sair == 'n':
        if id_produto in produtos.keys():
            exibir_produto(id_produto)

            resp = input("\n»› Tem certeza que deseja excluir este produto (S/N)? ").lower()

            if resp == "s":
                del produtos[id_produto]
                print("\n»› Produto excluido com sucesso! ")
            else:
                print("\n»› Não foi possível excluir o produto. ")
        else:
            print("\n»› Produto não encotrado. Tem certeza que ele está cadastrado?")
            
        sair = input('\n»› Deseja sair do módulo "Deletar Produto" (S/N)? ').lower()
        print()
        if sair == "n":
            id_produto = funcoes.ler_codigo('Digite o ID de cadastro do produto: ', produtos)
    print()
    input("»› Tecle <ENTER> para continuar... ")
