import pickle
from validacoes import validacoes
import interfaces as ifc
from dicionarios import clientes, produtos, vendas

# escerver o dicionario no arquivo
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
def lerNome():
    nome = input("##### Nome: ")
    while not validacoes.validarNome(nome):
        print("##### Ops! O nome informado é inválido! Tente novamente...")
        print()
        nome = input("##### Nome: ")
    nome = validacoes.validarNome(nome)
    return nome

def lerNomeRegex():
    nome = input("##### Nome: ")
    while not validacoes.validarNomeRegex(nome):
        print("##### Ops! O nome informado é inválido! Tente novamente...")
        print()
        nome = input("##### Nome: ")
    return nome

def lerTelefone():
    tel = input("##### Telefone: ")
    while not(validacoes.validarTelefone(tel)):
        print("##### Ops! O celular informado é inválido! Tente novamente...")
        print()
        tel = input("##### Telefone: ")
    return tel

def lerEmail():
    email = input("##### Email: ")
    while not(validacoes.validarEmail(email)):
        print("##### Ops! O Email informado é inválido! Tente novamente...")
        print()
        email = input("##### Email: ")
    return email

def lerQuantidade():
    qtd = input("##### Quantidade: ")
    while not validacoes.validarQuantidade(qtd):
        print("##### Ops! Aceitamos somete números! Tente novamente...")
        print()
        qtd = input("##### Quantidade: ")
    return qtd

def lerPreco():
    preco = input("##### Preço: ")
    while not validacoes.validarPreco(preco):
        print("##### Ops! Aceitamos somete números! Tente novamente...")
        print()
        preco = input("##### Preço: ")
    return preco

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

