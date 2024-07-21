import funcoes
import interfaces as ifc
from dicionarios import clientes


def exibir_cliente(id_cliente):
    print()
    cliente = clientes[id_cliente][0]
    telefone = clientes[id_cliente][1]
    email = clientes[id_cliente][2]
    endereco = clientes[id_cliente][3]
    rua = endereco["rua"]
    bairro = endereco["bairro"]
    num_casa = endereco["num_casa"]
    logradouro = f"R. {rua} {num_casa}, {bairro}"
    print('»› Informações do Cliente ‹«')
    print(f"»› Nome: {cliente}")
    print(f"»› Telefone: {telefone}")
    print(f"»› Email: {email}")
    print(f'»› Cidade: {endereco["cidade"]}')
    print(f"»› Endereço: {logradouro}")
    print("»› ID de cadastro: ", id_cliente)
    print()


def cadastrar_cliente():
    ifc.cabecalho_modulos("Cadastrar Cliente")
    nome_cliente = funcoes.ler_nome()
    telefone_cliente = funcoes.ler_telefone()
    email_cliente = funcoes.ler_email()
    cidade_cliente = funcoes.ler_cidade()
    bairro_cliente = funcoes.ler_logradouro("Nome do Bairro")
    rua_cliente = funcoes.ler_logradouro("Nome da Rua")
    num_casa_cliente = funcoes.ler_logradouro("Número da casa")

    id_cliente = funcoes.gerar_codigo(clientes)
    clientes[id_cliente] = [
        nome_cliente,
        telefone_cliente,
        email_cliente,
        {
            "cidade": cidade_cliente,
            "bairro": bairro_cliente,
            "rua": rua_cliente,
            "num_casa": num_casa_cliente,
        },
    ]

    exibir_cliente(id_cliente)
    print("»› Cliente cadastrado com sucesso!")
    print()
    input("»› Tecle <ENTER> para continuar... ")


def pesquisar_cliente():
    ifc.cabecalho_modulos("Pesquisar Cliente")
    id_cliente = funcoes.ler_codigo('Digite o ID de cadastro do cliente: ', clientes)
    sair = "n"
    while sair == "n":
        exibir_cliente(id_cliente)

        sair = input('\n»› Deseja sair do módulo "Pesquisar Cliente" (S/N)? ').lower()
        print()
        if sair == "n":
            id_cliente = funcoes.ler_codigo('Digite o ID de cadastro do cliente: ', clientes)
    print()
    input("»› Tecle <ENTER> para continuar... ")


def atualizar_cliente():
    ifc.cabecalho_modulos("Atualizar Cliente")
    id_cliente = funcoes.ler_codigo('Digite o ID de cadastro do cliente: ', clientes)
    sair = "n"
    while sair == "n":
        nome_cliente = funcoes.ler_nome()
        telefone_cliente = funcoes.ler_telefone()
        email_cliente = funcoes.ler_email()
        cidade_cliente = funcoes.ler_cidade()
        bairro_cliente = funcoes.ler_logradouro("Nome do Bairro")
        rua_cliente = funcoes.ler_logradouro("Nome da Rua")
        num_casa_cliente = funcoes.ler_logradouro("Número da casa")

        clientes[id_cliente] = [
            nome_cliente,
            telefone_cliente,
            email_cliente,
            {
                "cidade": cidade_cliente,
                "bairro": bairro_cliente,
                "rua": rua_cliente,
                "num_casa": num_casa_cliente,
            },
        ]
        print("»› Novos dados do cliente: ")
        exibir_cliente(id_cliente)
        print("»› Dados do cliente atualizado com sucesso!")

        sair = input('\n»› Deseja sair do módulo "Atualizar Cliente" (S/N)? ').lower()
        print()
        if sair == "n":
            id_cliente = funcoes.ler_codigo('Digite o ID de cadastro do cliente: ', clientes)
    print()
    input("»› Tecle <ENTER> para continuar... ")


def deletar_cliente():
    ifc.cabecalho_modulos("Deletar Cliente")
    id_cliente = funcoes.ler_codigo('Digite o ID de cadastro do cliente: ', clientes)
    sair = "n"
    while sair == "n":
        exibir_cliente(id_cliente)
        resp = input("»› Tem certeza que deseja remover este cliente (S/N)? ").lower()

        if resp != "n":
            del clientes[id_cliente]
            print("»› Cliente excluido com sucesso! ")
        else:
            print("»› Não foi possível excluir o cliente. ")

        sair = input('\n»› Deseja sair do módulo "Deletar Cliente" (S/N)? ').lower()
        print()
        if sair == "n":
            id_cliente = funcoes.ler_codigo('Digite o ID de cadastro do cliente: ', clientes)
    print()
    input("»› Tecle <ENTER> para continuar... ")
