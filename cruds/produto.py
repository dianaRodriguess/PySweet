import interfaces as ifc
from dicionarios import produtos
import funcoes


def exibir_produto(id_produto):
    produto = produtos[id_produto][0]
    quantidade = produtos[id_produto][1]
    preco = produtos[id_produto][2]

    print(f"Nome do produto: {produto}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço da unidade: R$ {preco}")
    print("Id de cadastro: ", id_produto)


def atualizar_quantidade(id_produto, qtd_vendida):
    qtd_produto = int(produtos[id_produto][1])
    qtd_atual = qtd_produto - qtd_vendida
    return qtd_atual


def cadastrar_produto():
    ifc.cabecalho_modulos("Cadastrar Produto")
    nome_produto = funcoes.ler_nome()
    print()
    qtd_produto = funcoes.ler_quantidade()
    print()
    preco_produto = funcoes.ler_preco()

    id_produto = produtos.__len__() + 1
    id_produto = str(id_produto)
    produtos[id_produto] = [nome_produto, qtd_produto, preco_produto]

    print()
    exibir_produto(id_produto)
    print("\nProduto cadastrado com sucesso!!")
    print()
    input("Tecle <ENTER> para continuar... ")


def pesquisar_produto():
    ifc.cabecalho_modulos("Pesquisar Produto")
    id_produto = input("Qual o id do produto? ")

    if id_produto in produtos.keys():
        print()
        exibir_produto(id_produto)
    else:
        print("Não foi possível achar o produto. Tem certeza que ele está cadastrado? ")
    print()
    input("Tecle <ENTER> para continuar... ")


def atualizar_produto():
    ifc.cabecalho_modulos("Atualizar Produto")
    id_produto = input("Qual o id do produto? ")
    print()

    if id_produto in produtos.keys():

        nome_produto = funcoes.ler_nome()
        print()
        qtd_produto = funcoes.ler_quantidade()
        print()
        preco_produto = funcoes.ler_preco()

        produtos[id_produto] = [nome_produto, qtd_produto, preco_produto]

        print()
        exibir_produto(id_produto)
        print()
    else:
        print(
            "Não foi possível encontrar o cliente. Tem certeza que ele está cadastrado?"
        )
    print()
    input("Tecle <ENTER> para continuar... ")


def deletar_produto():
    ifc.cabecalho_modulos("Deletar Produto")
    id_produto = input("Qual o id do produto? ")

    if id_produto in produtos.keys():
        exibir_produto(id_produto)

        resp = input("Tem certeza que deseja excluir este produto (S/N)? ").lower()

        if resp == "s":
            del produtos[id_produto]
            print("Produto excluido com sucesso! ")
        else:
            print("Não foi possível excluir o produto. ")
    else:
        print("Produto não encotrado. Tem certeza que ele está cadastrado?")
    print()
    input("Tecle <ENTER> para continuar... ")
