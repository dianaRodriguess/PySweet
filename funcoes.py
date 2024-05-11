import pickle
import os
import time
from datetime import datetime
from dicionarios import clientes, produtos, vendas

# def carregarArquivos():
#     try:
#         arq_clientes = open("clientes.dat", "rb")
#         clientes = pickle.load(arq_clientes)
#     except:
#         arq_clientes = open("clientes.dat", "wb")
#     arq_clientes.close()

# carregarArquivos()


def escreverArquivos():
    arq_clientes = open("clientes.dat", "wb")
    pickle.dump(clientes, arq_clientes)
    arq_clientes.close()

    arq_produtos = open("produtos.dat", "wb")
    pickle.dump(produtos, arq_produtos)
    arq_produtos.close()

    arq_vendas = open("vendas.dat", "wb")
    pickle.dump(vendas, arq_vendas)
    arq_vendas.close()


#########################
##### MENU PRICIPAL #####
#########################
def menuPrincipal():
    os.system("clear")
    print("############################################")
    print("######         Projeto PySweet        ######")
    print("############################################")
    print("#####      1 - Módulo Cadastrar        #####")
    print("#####      2 - Módulo Pesquisar        #####")
    print("#####      3 - Módulo Atualizar        #####")
    print("#####      4 - Módulo Deletar          #####")
    print("#####      5 - Módulo Relatório        #####")
    print("#####      6 - Módulo Informações      #####")
    print("#####      0 - Sair                    #####")
    op_mprinc = input("##### Escolha sua opção: ")
    return op_mprinc


############################
##### MÓDULO CADASTRAR #####
############################
def menuCadastrar():
    os.system("clear")
    print()
    print("############################################")
    print("#####         Módulo Cadastrar          ####")
    print("############################################")
    print("#####   1 - Cadastrar Cliente          #####")
    print("#####   2 - Cadastrar Venda            #####")
    print("#####   3 - Cadastrar Produto          #####")
    print("#####   0 - Sair                       #####")
    print()
    op_mcadas = input("##### Escolha sua opção: ")
    return op_mcadas


def cadastrarCliente():
    os.system("clear")
    print("############################################")
    print("#####           Cadastrar Cliente      #####")
    print("############################################")
    print()
    nome_cliente = input("##### Nome: ")
    print()
    telefone_cliente = input("##### Telefone: ")
    print()
    email_cliente = input("##### Email: ")
    print()
    endereço_cliente = input("##### Endereço: ")

    id = clientes.__len__() + 1
    id = str(id)
    clientes[id] = [
        nome_cliente, telefone_cliente, email_cliente, endereço_cliente
    ]

    cliente = clientes[id][0]
    telefone = clientes[id][1]
    email = clientes[id][2]
    endereco = clientes[id][3]
    print()
    print("Cliente cadastrado com sucesso!!")
    print()
    print(f"Nome: {cliente}")
    print(f"Telefone: {telefone}")
    print(f"Email: {email}")
    print(f"Endereço: {endereco}")
    print("Id de cadastro: ", id)
    print()

    input("Tecle <ENTER> para continuar... ")


# def calcularPreco():


def cadastrarVenda():
    os.system("clear")
    print("############################################")
    print("#####           Cadastrar Venda        #####")
    print("############################################")
    print()
    id_produto = input("##### Produto vendido: ")
    print()
    id_cliente = input("##### Cliente: ")
    print()
    qtd_vendida = input("##### Quantidade vendida: ")
    print()
    forma_pagamento = input(
        "##### Forma de pagamento: \n##### 1 - Cartão de Débito \n##### 2 - Cartão de Crédito \n##### 3 - Espécie \n##### 4 - PIX \n: "
    )

    if forma_pagamento == "1":
        forma_pagamento = "Cartão Débito"
    elif forma_pagamento == "2":
        forma_pagamento = "Cartão Crédito"
    elif forma_pagamento == "3":
        forma_pagamento = "Espécie"
    elif forma_pagamento == "4":
        forma_pagamento = "PIX"
    else:
        print("Forma de pagamento inválida. Retornaremos ao Menu Cadastrar")
        # time.sleep(3)
        # menuCadastrar()
    data = datetime.now()

    if id_produto in produtos.keys():
        if id_cliente in clientes.keys():

            id = vendas.__len__() + 1
            id = str(id)
            vendas[id] = [
                id_produto,
                id_cliente,
                qtd_vendida,
                forma_pagamento,
                data.strftime("%x, %X"),
            ]

            cliente = clientes[vendas[id][1]][0]
            produto = produtos[vendas[id][0]][0]
            print()
            print("Venda cadastrado com sucesso!!")
            print()
            print(f"Nome do cliente: {cliente}")
            print(f"Produto: {produto}")
            print(f"Quantidade: {qtd_vendida}")
            print(f"Forma de pagamento: {forma_pagamento}")
            print("Data: ", data.strftime("%x às %X"))
            print("Id de cadastro: ", id)
            print()
    else:
        print("Produto não encotrado. ")

    input("Tecle <ENTER> para continuar... ")


def cadastrarProduto():
    os.system("clear")
    print("############################################")
    print("#####           Cadastrar Produto      #####")
    print("############################################")
    print()
    nome_produto = input("Nome: ")
    print()
    qtd_produto = input("Quantidade: ")
    print()
    preco_produto = input("Preço: ")

    id = produtos.__len__() + 1
    id = str(id)
    produtos[id] = [nome_produto, qtd_produto, preco_produto]

    produto = produtos[id][0]
    quantidade = produtos[id][1]
    preco = produtos[id][2]

    print("\nProduto cadastrado com sucesso!!")
    print()
    print(f"Nome do produto: {produto}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço da unidade: R$ {preco}")
    print("Id de cadastro: ", id)
    print()
    input("Tecle <ENTER> para continuar... ")


############################
##### MÓDULO PESQUISAR #####
############################
def menuPesquisar():
    os.system("clear")
    print()
    print("############################################")
    print("#####          Módulo Pesquisar         ####")
    print("############################################")
    print("#####   1 - Pesquisar Cliente          #####")
    print("#####   2 - Pesquisar Venda            #####")
    print("#####   3 - Pesquisar Produto          #####")
    print("#####   0 - Sair                       #####")
    print()
    op_mpesq = input("##### Escolha sua opção: ")
    return op_mpesq


# TODO: deixar mais bonito
def pesquisarCliente():
    os.system("clear")
    print("############################################")
    print("#####          Pesquisar Cliente       #####")
    print("############################################")
    print()
    id_cliente = input("Qual o id do cliente? ")

    # # read
    # aqvjson = open("clientes.json", "r")
    # jsondata = aqvjson.read()

    # # parse
    # obj = json.loads(jsondata)
    # lista = obj[id_cliente]
    # cliente = lista[0]
    # telefone = lista[1]
    # email = lista[2]
    # endereço = lista[3]

    if id_cliente in clientes.keys():
        print()
        print("Nome: ", clientes[id_cliente][0])
        print("Telefone: ", clientes[id_cliente][1])
        print("Email: ", clientes[id_cliente][2])
        print("Endereço: ", clientes[id_cliente][3])
        print()
    else:
        print(
            "Não foi possível encontrar o cliente. Tem certeza que ele está cadastrado? "
        )
    input("Tecle <ENTER> para continuar... ")


def pesquisarVenda():
    os.system("clear")
    print("############################################")
    print("#####           Pesquisar Venda        #####")
    print("############################################")
    print()
    print(vendas)
    id_venda = input("Qual o id da venda? ")

    produto = produtos[vendas[id_venda][0]][0]
    cliente = clientes[vendas[id_venda][1]][0]

    if id_venda in vendas.keys():
        print()
        print("Comprador: ", cliente)
        print("Produto vendido: ", produto)
        print("Quantidade vendida: ", vendas[id_venda][2])
        print("Data: ", vendas[id_venda][3])
        print("Forma de pagamento: ", vendas[id_venda][4])
        print()
    input("Tecle <ENTER> para continuar... ")


def pesquisarProduto():
    os.system("clear")
    print("############################################")
    print("#####           Pesquisar Produto      #####")
    print("############################################")
    print()
    id_produto = input("Qual o id do produto? ")

    if id_produto in produtos.keys():
        print()
        print("Produto: ", produtos[id_produto][0])
        print("Quantidade: ", produtos[id_produto][1])
        print("Preço: ", produtos[id_produto][2])
        print()
    input("Tecle <ENTER> para continuar... ")


############################
##### MÓDULO ATUALIZAR #####
############################
def menuAtualizar():
    os.system("clear")
    print()
    print("############################################")
    print("#####         Módulo Atualizar          ####")
    print("############################################")
    print("#####   1 - Atualizar Cliente          #####")
    print("#####   2 - Atualizar Venda            #####")
    print("#####   3 - Atualizar Produto          #####")
    print("#####   0 - Sair                       #####")
    print()
    op_matua = input("##### Escolha sua opção: ")
    return op_matua


def atualizarCliente():
    os.system("clear")
    print("############################################")
    print("#####           Atualizar Cliente      #####")
    print("############################################")
    print()
    id_cliente = input("Qual o id do cliente? ")

    if id_cliente in clientes.keys():
        print()
        nome_cliente = input("##### Nome: ")
        print()
        telefone_cliente = input("##### Telefone: ")
        print()
        email_cliente = input("##### Email: ")
        print()
        endereço_cliente = input("##### Endereço: ")

        clientes[id_cliente] = [
            nome_cliente, telefone_cliente, email_cliente, endereço_cliente
        ]

        cliente = clientes[id_cliente][0]
        telefone = clientes[id_cliente][1]
        email = clientes[id_cliente][2]
        endereco = clientes[id_cliente][3]
        print()
        print("Cliente cadastrado com sucesso!!")
        print()
        print(f"Nome: {cliente}")
        print(f"Telefone: {telefone}")
        print(f"Email: {email}")
        print(f"Endereço: {endereco}")
        print("Id de cadastro: ", id_cliente)
        print()
    else:
        print(
            "Não foi possível encontrar o cliente. Tem certeza que ele está cadastrado?"
        )

    input("Tecle <ENTER> para continuar... ")


def atualizarVenda():
    os.system("clear")
    print("############################################")
    print("#####           Atualizar Venda        #####")
    print("############################################")
    print()
    id_venda = input("Qual o id da venda? ")
    print()

    if id_venda in vendas.keys():
        id_produto = input("##### Produto vendido: ")
        print()
        id_cliente = input("##### Cliente: ")
        print()
        qtd_vendida = input("##### Quantidade vendida: ")
        print()
        forma_pagamento = input("##### Forma de pagamento: \n##### 1 - Cartão de Débito \n##### 2 - Cartão de Crédito \n##### 3 - Espécie \n##### 4 - PIX \n: ")

        if forma_pagamento == "1":
            forma_pagamento = "Cartão Débito"
        elif forma_pagamento == "2":
            forma_pagamento = "Cartão Crédito"
        elif forma_pagamento == "3":
            forma_pagamento = "Espécie"
        elif forma_pagamento == "4":
            forma_pagamento = "PIX"
        else:
            print("Forma de pagamento inválida. Retornaremos ao Menu Cadastrar")
            input("Tecle <ENTER> para voltar ao menu... ")

        data = datetime.now()

        if id_produto in produtos.keys():
            if id_cliente in clientes.keys():
                vendas[id_venda] = [
                    id_produto,
                    id_cliente,
                    qtd_vendida,
                    forma_pagamento,
                    data.strftime("%x, %X"),
                ]

                cliente = clientes[vendas[id_venda][1]][0]
                produto = produtos[vendas[id_venda][0]][0]
                print()
                print("Venda cadastrado com sucesso!!")
                print()
                print(f"Nome do cliente: {cliente}")
                print(f"Produto: {produto}")
                print(f"Quantidade: {qtd_vendida}")
                print(f"Forma de pagamento: {forma_pagamento}")
                print("Data: ", data.strftime("%x às %X"))
                print("Id de cadastro: ", id_venda)
                print()
            else:
                print("Cliente não encontrado. ")
                print()
        else: 
            print("Produto não encontrado. ")
            print()
    input("Tecle <ENTER> para continuar... ")


def atualizarProduto():
    os.system("clear")
    print("############################################")
    print("#####           Atualizar Produto      #####")
    print("############################################")
    print()
    id_produto = input("Qual o id do produto? ")
    print()

    if id_produto in produtos.keys():

        nome_produto = input("Nome: ")
        print()
        qtd_produto = input("Quantidade: ")
        print()
        preco_produto = input("Preço: ")

        produtos[id_produto] = [nome_produto, qtd_produto, preco_produto]

        produto = produtos[id_produto][0]
        quantidade = produtos[id_produto][1]
        preco = produtos[id_produto][2]

        print()
        print(f"Nome do produto: {produto}")
        print(f"Quantidade: {quantidade}")
        print(f"Preço da unidade: R$ {preco}")
        print("Id de cadastro: ", id_produto)
        print()
        input("Tecle <ENTER> para continuar... ")


##########################
##### MÓDULO DELETAR #####
##########################
def menuDeletar():
    os.system("clear")
    print()
    print("############################################")
    print("#####           Módulo Deletar          ####")
    print("############################################")
    print("#####   1 - Deletar Cliente            #####")
    print("#####   2 - Deletar Venda              #####")
    print("#####   3 - Deletar Produto            #####")
    print("#####   0 - Sair                       #####")
    print()
    op_mdele = input("##### Escolha sua opção: ")
    return op_mdele


def deletarCliente():
    os.system("clear")
    print("############################################")
    print("#####           Deletar Cliente        #####")
    print("############################################")
    print()
    input("Tecle <ENTER> para continuar... ")


def deletarVenda():
    os.system("clear")
    print("############################################")
    print("#####           Deletar Venda        #####")
    print("############################################")
    print()
    input("Tecle <ENTER> para continuar... ")


def deletarProduto():
    os.system("clear")
    print("############################################")
    print("#####           Deletar Produto        #####")
    print("############################################")
    print()
    input("Tecle <ENTER> para continuar... ")


############################
##### MÓDULO RELATÓRIO #####
############################
def menuRelatorio():
    os.system("clear")
    print()
    print("############################################")
    print("#####   Você está no Módulo Relatório   ####")
    print("############################################")
    print("#####   1 - Produtos mais vendidos     #####")
    print("#####   2 - Produtos menos vendidos    #####")
    print("#####   3 - Produtos com maior estoque #####")
    print("#####   4 - Produtos com menor estoque #####")
    print("#####   5 - Maiores compradores        #####")
    print("#####   6 - Datas que mais vendem      #####")
    print("#####   0 - Sair                       #####")
    print()
    op_mrela = input("##### Escolha sua opção: ")
    return op_mrela


def prdtMaisVend():
    os.system("clear")
    print("#################################################")
    print("#####         Produtos Mais Vendidos        #####")
    print("#################################################")
    print()
    input("Tecle <ENTER> para continuar... ")


def prdtMenosVend():
    os.system("clear")
    print("#################################################")
    print("#####        Produtos Menos Vendidos        #####")
    print("#################################################")
    print()
    input("Tecle <ENTER> para continuar... ")


def prdtMaisEstoque():
    os.system("clear")
    print("#################################################")
    print("#####      Produtos Com Maior Estoque       #####")
    print("#################################################")
    print()
    input("Tecle <ENTER> para continuar... ")


def prdtMenosEstoque():
    os.system("clear")
    print("#################################################")
    print("#####      Produtos Com Menor Estoque       #####")
    print("#################################################")
    print()
    input("Tecle <ENTER> para continuar... ")


def maioresCompradores():
    os.system("clear")
    print("#################################################")
    print("#####         Maiores Compradores           #####")
    print("#################################################")
    print()
    input("Tecle <ENTER> para continuar... ")


def dtMaisVendem():
    os.system("clear")
    print("#################################################")
    print("#####         Datas Que Mais Vendem         #####")
    print("#################################################")
    print()
    input("Tecle <ENTER> para continuar... ")


##############################
##### MÓDULO INFORMAÇÕES #####
##############################
def informacoes():
    os.system("clear")
    print()
    print("######################################################")
    print("#####       Você está no Módulo Informações      #####")
    print("######################################################")
    print()
    print("##### Projeto de Gestão de uma Fábrica de doces   ####")
    print("##### Equipe de desenvolvimento:                  ####")
    print("##### Diana Rodrigues @dianarodrigues3            ####")
    print("##### Flavius Gorgônio @flgorgonio                ####")
    print("##### Licença Pública Geral GNU                   ####")
    print("##### www.gnu.org/licenses/gpl.html               ####")
    print()
    input("Tecle <ENTER> para continuar... ")
    # op_minfo = input("Tecle <ENTER> para continuar... ")
    # return op_minfo


escreverArquivos()
