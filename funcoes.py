import pickle
import interfaces as ifc
from datetime import datetime
from dicionarios import clientes, produtos, vendas


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
    ifc.interfaceMenuPrincipal()
    op_mprinc = input("##### Escolha sua opção: ")
    return op_mprinc

############################
##### MÓDULO CADASTRAR #####
############################
def menuCadastrar():
    ifc.interfaceMenuCadastrar()
    op_mcadas = input("##### Escolha sua opção: ")
    return op_mcadas

def cadastrarCliente():
    ifc.cabecalhoModulos("Cadastrar Cliente")
    nome_cliente = input("##### Nome: ")
    print()
    telefone_cliente = input("##### Telefone: ")
    print()
    email_cliente = input("##### Email: ")
    print()
    endereço_cliente = input("##### Endereço: ")

    id_cliente = clientes.__len__() + 1
    id_cliente = str(id_cliente)
    clientes[id_cliente] = [nome_cliente, telefone_cliente, email_cliente, endereço_cliente]

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
    input("Tecle <ENTER> para continuar... ")

def cadastrarVenda():
    ifc.cabecalhoModulos("Cadastrar Venda")
    id_produto = input("##### Produto vendido: ")
    print()
    id_cliente = input("##### Cliente: ")
    print()
    qtd_vendida = input("##### Quantidade vendida: ")
    print()
    valor_total = input("##### Total: ")
    forma_pagamento = input("##### Forma de pagamento: \n##### 1 - Cartão de Débito \n##### 2 - Cartão de Crédito \n##### 3 - Espécie \n##### 4 - PIX \n: " )

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

            id_venda = vendas.__len__() + 1
            id_venda = str(id_venda)
            vendas[id_venda] = [id_produto,id_cliente,qtd_vendida,forma_pagamento,valor_total,data.strftime("%x, %X"),]

            cliente = clientes[vendas[id_venda][1]][0]
            produto = produtos[vendas[id_venda][0]][0]
            print()
            print("Venda cadastrado com sucesso!!")
            print()
            print(f"Nome do cliente: {cliente}")
            print(f"Produto: {produto}")
            print(f"Quantidade: {qtd_vendida}")
            print(f"Forma de pagamento: {forma_pagamento}")
            print(f"Total: {valor_total}")
            print("Data: ", data.strftime("%x às %X"))
            print("Id de cadastro: ", id_venda)
        else:
            print("Cliente não encontrado. ")
    else:
        print("Produto não encotrado. ")
    print()
    input("Tecle <ENTER> para continuar... ")

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

    produto = produtos[id_produto][0]
    quantidade = produtos[id_produto][1]
    preco = produtos[id_produto][2]

    print("\nProduto cadastrado com sucesso!!")
    print()
    print(f"Nome do produto: {produto}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço da unidade: R$ {preco}")
    print("Id de cadastro: ", id_produto)
    print()
    input("Tecle <ENTER> para continuar... ")

############################
##### MÓDULO PESQUISAR #####
############################
def menuPesquisar():
    ifc.interfaceMenuPesquisar()
    op_mpesq = input("##### Escolha sua opção: ")
    return op_mpesq

def pesquisarCliente():
    ifc.cabecalhoModulos("Pesquisar Cliente")
    id_cliente = input("Qual o id do cliente? ")

    if id_cliente in clientes.keys():
        print()
        print("Nome: ", clientes[id_cliente][0])
        print("Telefone: ", clientes[id_cliente][1])
        print("Email: ", clientes[id_cliente][2])
        print("Endereço: ", clientes[id_cliente][3])
        print()
    else:
        print("Não foi possível encontrar o cliente. Tem certeza que ele está cadastrado? " )
    print()
    input("Tecle <ENTER> para continuar... ")

def pesquisarVenda():
    ifc.cabecalhoModulos("Pesquisar Venda")
    id_venda = input("Qual o id da venda? ")

    produto = produtos[vendas[id_venda][0]][0]
    cliente = clientes[vendas[id_venda][1]][0]

    if id_venda in vendas.keys():
        print()
        print("Comprador: ", cliente)
        print("Produto vendido: ", produto)
        print("Quantidade vendida: ", vendas[id_venda][2])
        print("Forma de pagamento: ", vendas[id_venda][3])
        print("Total: ", vendas[id_venda][4])
        print("Data: ", vendas[id_venda][5])
        print()
    else:
        print("Não foi possível achar a venda. Tem certeza que ela está cadastrada? ")
    print()
    input("Tecle <ENTER> para continuar... ")

def pesquisarProduto():
    ifc.cabecalhoModulos("Pesquisar Produto")
    id_produto = input("Qual o id do produto? ")

    if id_produto in produtos.keys():
        print()
        print("Produto: ", produtos[id_produto][0])
        print("Quantidade: ", produtos[id_produto][1])
        print("Preço: ", produtos[id_produto][2])
    else:
        print("Não foi possível achar o produto. Tem certeza que ele está cadastrado? ")
    print()
    input("Tecle <ENTER> para continuar... ")

############################
##### MÓDULO ATUALIZAR #####
############################
def menuAtualizar():
    ifc.interfaceMenuAtualizar()
    op_matua = input("##### Escolha sua opção: ")
    return op_matua

def atualizarCliente():
    ifc.cabecalhoModulos("Atualizar Cliente")
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

        clientes[id_cliente] = [nome_cliente,telefone_cliente,email_cliente,endereço_cliente,]

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
    else:
        print("Não foi possível encontrar o cliente. Tem certeza que ele está cadastrado?")
    print()
    input("Tecle <ENTER> para continuar... ")

def atualizarVenda():
    ifc.cabecalhoModulos("Atualizar Venda")
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
        valor_total = input("##### valor_total: ")
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

        if id_produto in produtos.keys():
            if id_cliente in clientes.keys():
                vendas[id_venda] = [id_produto,id_cliente, qtd_vendida,forma_pagamento,valor_total,data]

                cliente = clientes[vendas[id_venda][1]][0]
                produto = produtos[vendas[id_venda][0]][0]
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
            else:
                print("Cliente não encontrado. ")
        else:
            print("Produto não encontrado. ")
    else:
        print("Não foi possível encontrar a venda. Tem certeza que ela está cadastrada?")
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

        produto = produtos[id_produto][0]
        quantidade = produtos[id_produto][1]
        preco = produtos[id_produto][2]

        print()
        print(f"Nome do produto: {produto}")
        print(f"Quantidade: {quantidade}")
        print(f"Preço da unidade: R$ {preco}")
        print("Id de cadastro: ", id_produto)
        print()
    else:
        print("Não foi possível encontrar o cliente. Tem certeza que ele está cadastrado?")
    print()
    input("Tecle <ENTER> para continuar... ")

##########################
##### MÓDULO DELETAR #####
##########################
def menuDeletar():
    ifc.interfaceMenuDeletar()
    op_mdele = input("##### Escolha sua opção: ")
    return op_mdele

def deletarCliente():
    ifc.cabecalhoModulos("Deletar Cliente")
    id_cliente = input("Qual o id do cliente? ")
    print()
    
    if id_cliente in clientes.keys():
        print("Nome: ", clientes[id_cliente][0])
        print("Telefone: ", clientes[id_cliente][1])
        print("Email: ", clientes[id_cliente][2])
        print("Endereço: ", clientes[id_cliente][3])
        
        resp = input("\nTem certeza que deseja deletar este cliente (S/N)? ").lower()
        
        if resp == "s":
            del clientes[id_cliente]
            print("Cliente excluido com sucesso! ")
        else: 
            print("Não foi possível excluir o cliente. ")
    else:
        print("Cliente não encontrado. Tem certeza que ele está cadastrado?")
    
    print()    
    input("Tecle <ENTER> para continuar... ")

def deletarVenda():
    ifc.cabecalhoModulos("Deletar Venda")
    id_venda = input("Qual o id da venda? ")
    
    produto = produtos[vendas[id_venda][0]][0]
    cliente = clientes[vendas[id_venda][1]][0]

    if id_venda in vendas.keys():
        print()
        print("Comprador: ", cliente)
        print("Produto vendido: ", produto)
        print("Quantidade vendida: ", vendas[id_venda][2])
        print("Forma de pagamento: ", vendas[id_venda][3])
        print("Data: ", vendas[id_venda][4])
        
        resp = input("Tem certeza que deseja excluir esta venda (S/N)? ").lower()
        
        if resp == 's':
            del vendas[id_venda]
            print("Venda excluida com sucesso! ")
        else:
            print("Não foi possível excluir a venda. ")
    else:
        print("Venda não encontrada. Tem certeza que ela está cadastrada?")      
    print()
    input("Tecle <ENTER> para continuar... ")

def deletarProduto():
    ifc.cabecalhoModulos("Deletar Produto")
    id_produto = input("Qual o id do produto? ")
    
    if id_produto in produtos.keys():
        print("Nome: ", produtos[id_produto][0])
        print("Quantidade: ", produtos[id_produto][1])
        print("Preço: ", produtos[id_produto][2])
        
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

############################
##### MÓDULO RELATÓRIO #####
############################
def menuRelatorio():
    ifc.interfaceMenuRelatorio()
    op_mrela = input("##### Escolha sua opção: ")
    return op_mrela

def exibirClientes():
    ifc.interfaceExibirClientes()
    for cliente in clientes:
        print("| %-4s "%(cliente), end='')
        print("| %-27s "%(clientes[cliente][0]), end='')
        print("| %-18s "%(clientes[cliente][1]), end='')
        print("| %-26s "%(clientes[cliente][2]), end='')
        print("| %-25s |"%(clientes[cliente][3])) 
    print("|------|-----------------------------|--------------------|----------------------------|---------------------------|")
    print()
    input("Tecle <ENTER> para continuar... ")

def exibirVendas():
    ifc.interfaceExibirVendas()
    for venda in vendas:
        cliente = clientes[vendas[venda][1]][0]
        produto = produtos[vendas[venda][0]][0]
        print("| %-4s "%(venda), end='')
        print("| %-26s "%(cliente), end='')
        print("| %-23s "%(produto), end='')
        print("| %-13s "%(vendas[venda][2]), end='')
        print("| %-16s "%(vendas[venda][3]), end='')
        print("| %-10s "%(vendas[venda][4]), end='')
        print("| %-16s |"%(vendas[venda][5]))
        
    print("|------|----------------------------|-------------------------|---------------|------------------|------------|--------------------|")
    print()
    input("Tecle <ENTER> para continuar... ")

def exibirProdutos():
    ifc.interfaceExibirProdutos()
    for produto in produtos:
        print("| %-4s "%(produto), end='')
        print("| %-27s "%(produtos[produto][0]), end='')
        print("| %-18s "%(produtos[produto][1]), end='')
        print("| %-15s |"%(produtos[produto][2]))
    print("|------|-----------------------------|--------------------|-----------------|")
    print()
    input("Tecle <ENTER> para continuar... ")
    
def prdtMaisVend():
    ifc.interfaceProdutosVendidos()
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
                print("| %-27s "%produtos[p][0], end='')
                print("| %-18s |"%produtos_vendidos[p])
    print("|-----------------------------|--------------------|")
    print()   
    input("Tecle <ENTER> para continuar... ")

def maioresCompradores():
    ifc.interfaceMaioresCompradores()
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
                print("| %-27s "%clientes[c][0], end='')
                print("| %-18s |"%maiores_compradores[c])
    print("|-----------------------------|--------------------|")
    print()   
    input("Tecle <ENTER> para continuar... ")

##############################
##### MÓDULO INFORMAÇÕES #####
##############################
def informacoes():
    ifc.interfaceInformacoes()
    input("Tecle <ENTER> para continuar... ")

escreverArquivos()
