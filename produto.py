import interfaces as ifc
from dicionarios import produtos

def exibirProduto(id_produto):
    produto = produtos[id_produto][0]
    quantidade = produtos[id_produto][1]
    preco = produtos[id_produto][2]
    
    print(f"Nome do produto: {produto}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço da unidade: R$ {preco}")
    print("Id de cadastro: ", id_produto)

def cadastrarProduto():
    ifc.cabecalhoModulos("Cadastrar Produto")
    nome_produto = input("##### Nome: ")
    print()
    qtd_produto = input("##### Quantidade: ")
    print()
    preco_produto = input("##### Preço: ")

    id_produto = produtos.__len__() + 1
    id_produto = str(id_produto)
    produtos[id_produto] = [nome_produto, qtd_produto, preco_produto]

    print()
    exibirProduto(id_produto)
    print("\nProduto cadastrado com sucesso!!")
    print()
    input("Tecle <ENTER> para continuar... ")

def pesquisarProduto():
    ifc.cabecalhoModulos("Pesquisar Produto")
    id_produto = input("Qual o id do produto? ")

    if id_produto in produtos.keys():
        print()
        exibirProduto(id_produto)
    else:
        print("Não foi possível achar o produto. Tem certeza que ele está cadastrado? ")
    print()
    input("Tecle <ENTER> para continuar... ")

def atualizarProduto():
    ifc.cabecalhoModulos("Atualizar Produto")
    id_produto = input("Qual o id do produto? ")
    print()

    if id_produto in produtos.keys():

        nome_produto = input("Nome: ")
        print()
        qtd_produto = input("Quantidade: ")
        print()
        preco_produto = input("Preço: ")

        produtos[id_produto] = [nome_produto, qtd_produto, preco_produto]

        print()
        exibirProduto(id_produto)
        print()
    else:
        print("Não foi possível encontrar o cliente. Tem certeza que ele está cadastrado?")
    print()
    input("Tecle <ENTER> para continuar... ")

def deletarProduto():
    ifc.cabecalhoModulos("Deletar Produto")
    id_produto = input("Qual o id do produto? ")

    if id_produto in produtos.keys():
        exibirProduto(id_produto)

        resp = input("Tem certeza que deseja excluir este produto (S/N)? ").lower()

        if resp == 's':
            del produtos[id_produto]
            print("Produto excluido com sucesso! ")
        else: 
            print("Não foi possível excluir o produto. ")
    else:
        print("Produto não encotrado. Tem certeza que ele está cadastrado?")
    print()    
    input("Tecle <ENTER> para continuar... ")
