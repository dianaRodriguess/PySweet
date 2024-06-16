import pickle
import interfaces as ifc
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
#####  FUNÇÕES LER  #####
#########################
# def lerNome():
# def lerTelefone():
# def lerEmail():
# def lerEndereço():

#########################
#####     MENUS     #####
#########################
def menuPrincipal():
    ifc.interfaceMenuPrincipal()
    op_mprinc = input("##### Escolha sua opção: ")
    return op_mprinc

##### MÓDULO CADASTRAR #####
def menuCadastrar():
    ifc.interfaceMenuCadastrar()
    op_mcadas = input("##### Escolha sua opção: ")
    return op_mcadas

##### MÓDULO PESQUISAR #####
def menuPesquisar():
    ifc.interfaceMenuPesquisar()
    op_mpesq = input("##### Escolha sua opção: ")
    return op_mpesq

##### MÓDULO ATUALIZAR #####
def menuAtualizar():
    ifc.interfaceMenuAtualizar()
    op_matua = input("##### Escolha sua opção: ")
    return op_matua

##### MÓDULO DELETAR #####
def menuDeletar():
    ifc.interfaceMenuDeletar()
    op_mdele = input("##### Escolha sua opção: ")
    return op_mdele

##### MÓDULO RELATÓRIO #####
def menuRelatorio():
    ifc.interfaceMenuRelatorio()
    op_mrela = input("##### Escolha sua opção: ")
    return op_mrela

##############################
#####     INFORMAÇÕES    #####
##############################
def informacoes():
    ifc.interfaceInformacoes()
    input("Tecle <ENTER> para continuar... ")

