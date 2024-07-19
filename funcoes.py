import pickle
import re
from validacoes import validacoes
import interfaces as ifc
from dicionarios import clientes, produtos, vendas


# escerver o dicionario no arquivo
def escrever_arquivos():
    arq_clientes = open("data/clientes.dat", "wb")
    pickle.dump(clientes, arq_clientes)
    arq_clientes.close()

    arq_produtos = open("data/produtos.dat", "wb")
    pickle.dump(produtos, arq_produtos)
    arq_produtos.close()

    arq_vendas = open("data/vendas.dat", "wb")
    pickle.dump(vendas, arq_vendas)
    arq_vendas.close()


#########################
#####  FUNÇÕES LER  #####
#########################
def ler_nome():
    nome = input("##### Nome: ")
    while not validacoes.validar_nome(nome):
        print("##### Ops! O nome informado é inválido! Tente novamente...")
        print()
        nome = input("##### Nome: ")
    nome = nome.strip().title()
    nome = re.sub(r"\s+", " ", nome)
    return nome


def ler_nome_regex():
    nome = input("##### Nome: ")
    while not validacoes.validar_nome_regex(nome):
        print("##### Ops! O nome informado é inválido! Tente novamente...")
        print()
        nome = input("##### Nome: ")
    return nome


def ler_telefone():
    tel = input("##### Telefone: ")
    while not (validacoes.validar_telefone(tel)):
        print("##### Ops! O celular informado é inválido! Tente novamente...")
        print()
        tel = input("##### Telefone: ")
    return tel


def ler_email():
    email = input("##### Email: ")
    while not (validacoes.validar_email(email)):
        print("##### Ops! O Email informado é inválido! Tente novamente...")
        print()
        email = input("##### Email: ")
    return email


def ler_quantidade():
    qtd = input("##### Quantidade: ")
    while not validacoes.validar_quantidade(qtd):
        print("##### Ops! Aceitamos somete números! Tente novamente...")
        print()
        qtd = input("##### Quantidade: ")
    return qtd


def ler_preco():
    preco = input("##### Preço: ")
    while not validacoes.validar_preco(preco):
        print("##### Ops! Aceitamos somete números! Tente novamente...")
        print()
        preco = input("##### Preço: ")
    return preco


# def lerEndereço():


#########################
#####     MENUS     #####
#########################
def menu_principal():
    ifc.interface_menu_principal()
    op_mprinc = input("##### Escolha sua opção: ")
    return op_mprinc


##### MÓDULO CADASTRAR #####
def menu_cadastrar():
    ifc.interface_menu_cadastrar()
    op_mcadas = input("##### Escolha sua opção: ")
    return op_mcadas


##### MÓDULO PESQUISAR #####
def menu_pesquisar():
    ifc.interface_menu_pesquisar()
    op_mpesq = input("##### Escolha sua opção: ")
    return op_mpesq


##### MÓDULO ATUALIZAR #####
def menu_atualizar():
    ifc.interface_menu_atualizar()
    op_matua = input("##### Escolha sua opção: ")
    return op_matua


##### MÓDULO DELETAR #####
def menu_deletar():
    ifc.interface_menu_deletar()
    op_mdele = input("##### Escolha sua opção: ")
    return op_mdele


##### MÓDULO RELATÓRIO #####
def menu_relatorio():
    ifc.interface_menu_relatorio()
    op_mrela = input("##### Escolha sua opção: ")
    return op_mrela


##############################
#####     INFORMAÇÕES    #####
##############################
def informacoes():
    ifc.interface_informacoes()
    input("Tecle <ENTER> para continuar... ")
