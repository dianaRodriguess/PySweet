import funcoes
import interfaces as ifc
from dicionarios import clientes

def exibirCliente(id_cliente):
    cliente = clientes[id_cliente][0]
    telefone = clientes[id_cliente][1]
    email = clientes[id_cliente][2]
    endereco = clientes[id_cliente][3]
    print()
    print(f"Nome: {cliente}")
    print(f"Telefone: {telefone}")
    print(f"Email: {email}")
    print(f"Endereço: {endereco}")
    print("Id de cadastro: ", id_cliente)
    
def cadastrarCliente():
    ifc.cabecalhoModulos("Cadastrar Cliente")
    nome_cliente = funcoes.lerNomeRegex()
    print()
    telefone_cliente = funcoes.lerTelefone()
    print()
    email_cliente = funcoes.lerEmail()
    print()
    endereço_cliente = input("##### Endereço: ")

    id_cliente = clientes.__len__() + 1
    id_cliente = str(id_cliente)
    clientes[id_cliente] = [nome_cliente, telefone_cliente, email_cliente, endereço_cliente]

    exibirCliente(id_cliente)
    print("\nCliente cadastrado com sucesso!")
    print()
    input("Tecle <ENTER> para continuar... ")

def pesquisarCliente():
    ifc.cabecalhoModulos("Pesquisar Cliente")
    id_cliente = input("Qual o id do cliente? ")

    if id_cliente in clientes.keys():
        print()
        exibirCliente(id_cliente)
        print()
    else:
        print("Não foi possível encontrar o cliente. Tem certeza que ele está cadastrado? " )
    print()
    input("Tecle <ENTER> para continuar... ")

def atualizarCliente():
    ifc.cabecalhoModulos("Atualizar Cliente")
    id_cliente = input("Qual o id do cliente? ")

    if id_cliente in clientes.keys():
        print()
        nome_cliente = funcoes.lerNomeRegex()
        print()
        telefone_cliente = funcoes.lerTelefone()
        print()
        email_cliente = funcoes.lerEmail()
        print()
        endereço_cliente = input("##### Endereço: ")

        clientes[id_cliente] = [nome_cliente,telefone_cliente,email_cliente,endereço_cliente]
        exibirCliente(id_cliente)
        print("\nDados do Cliente adualizado com sucesso!")
    else:
        print("Não foi possível encontrar o cliente. Tem certeza que ele está cadastrado?")
    print()
    input("Tecle <ENTER> para continuar... ")

def deletarCliente():
    ifc.cabecalhoModulos("Deletar Cliente")
    id_cliente = input("Qual o id do cliente? ")
    print()

    if id_cliente in clientes.keys():
        exibirCliente(id_cliente)

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
