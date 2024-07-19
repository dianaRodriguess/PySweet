import funcoes
import interfaces as ifc
from dicionarios import clientes


def exibir_cliente(id_cliente):
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


def cadastrar_cliente():
    ifc.cabecalho_modulos("Cadastrar Cliente")
    nome_cliente = funcoes.ler_nome()
    print()
    telefone_cliente = funcoes.ler_telefone()
    print()
    email_cliente = funcoes.ler_email()
    print()
    endereço_cliente = input("##### Endereço: ")

    id_cliente = clientes.__len__() + 1
    id_cliente = str(id_cliente)
    clientes[id_cliente] = [
        nome_cliente,
        telefone_cliente,
        email_cliente,
        endereço_cliente,
    ]

    exibir_cliente(id_cliente)
    print("\nCliente cadastrado com sucesso!")
    print()
    input("Tecle <ENTER> para continuar... ")


def pesquisar_cliente():
    ifc.cabecalho_modulos("Pesquisar Cliente")
    id_cliente = input("Qual o id do cliente? ")

    if id_cliente in clientes.keys():
        print()
        exibir_cliente(id_cliente)
        print()
    else:
        print(
            "Não foi possível encontrar o cliente. Tem certeza que ele está cadastrado? "
        )
    print()
    input("Tecle <ENTER> para continuar... ")


def atualizar_cliente():
    ifc.cabecalho_modulos("Atualizar Cliente")
    id_cliente = input("Qual o id do cliente? ")

    if id_cliente in clientes.keys():
        print()
        nome_cliente = funcoes.ler_nome_regex()
        print()
        telefone_cliente = funcoes.ler_telefone()
        print()
        email_cliente = funcoes.ler_email()
        print()
        endereço_cliente = input("##### Endereço: ")

        clientes[id_cliente] = [
            nome_cliente,
            telefone_cliente,
            email_cliente,
            endereço_cliente,
        ]
        exibir_cliente(id_cliente)
        print("\nDados do Cliente adualizado com sucesso!")
    else:
        print(
            "Não foi possível encontrar o cliente. Tem certeza que ele está cadastrado?"
        )
    print()
    input("Tecle <ENTER> para continuar... ")


def deletar_cliente():
    ifc.cabecalho_modulos("Deletar Cliente")
    id_cliente = input("Qual o id do cliente? ")
    print()

    if id_cliente in clientes.keys():
        exibir_cliente(id_cliente)

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
