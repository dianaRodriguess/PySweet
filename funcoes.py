import os
from dicionarios import clientes, produtos, vendas


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
    op_mcadas = input("Tecle <ENTER> para continuar... ")
    return op_mcadas


def cadastrarCliente():
    os.system("clear")
    print("############################################")
    print("#####           Cadastrar Cliente      #####")
    print("############################################")
    print()
    nome = input("##### Nome: ")
    print()
    telefone = input("##### Telefone: ")
    print()
    email = input("##### Email: ")
    print()
    endereço = input("##### Endereço: ")

    id = clientes.__len__() + 1
    #   id = clientes
    id = str(id)
    clientes[id] = [nome, telefone, email, endereço]
    #   print(type(id))
    #   clientes.update({f"{id}": [nome, telefone, email, endereço]})
    print(clientes)
    print("Cliente cadastrado com sucesso!!")
    input("Tecle <ENTER> para continuar... ")


def cadastrarVenda():
    os.system("clear")
    print("############################################")
    print("#####           Cadastrar Venda        #####")
    print("############################################")
    print()
    input("Tecle <ENTER> para continuar... ")


def cadastrarProduto():
    os.system("clear")
    print("############################################")
    print("#####           Cadastrar Produto      #####")
    print("############################################")
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
    op_mpesq = input("Tecle <ENTER> para continuar... ")
    return op_mpesq


def pesquisarCliente():
    os.system("clear")
    print("############################################")
    print("#####          Pesquisar Cliente       #####")
    print("############################################")
    print()
    input("Tecle <ENTER> para continuar... ")


def pesquisarVenda():
    os.system("clear")
    print("############################################")
    print("#####           Pesquisar Venda        #####")
    print("############################################")
    print()
    input("Tecle <ENTER> para continuar... ")


def pesquisarProduto():
    os.system("clear")
    print("############################################")
    print("#####           Pesquisar Produto      #####")
    print("############################################")
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
    op_matua = input("Tecle <ENTER> para continuar... ")
    return op_matua


def atualizarCliente():
    os.system("clear")
    print("############################################")
    print("#####           Atualizar Cliente      #####")
    print("############################################")
    print()
    input("Tecle <ENTER> para continuar... ")


def atualizarVenda():
    os.system("clear")
    print("############################################")
    print("#####           Atualizar Venda        #####")
    print("############################################")
    print()
    input("Tecle <ENTER> para continuar... ")


def atualizarProduto():
    os.system("clear")
    print("############################################")
    print("#####           Atualizar Produto      #####")
    print("############################################")
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
    op_mdele = input("Tecle <ENTER> para continuar... ")
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
    op_mrela = input("Tecle <ENTER> para continuar... ")
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
