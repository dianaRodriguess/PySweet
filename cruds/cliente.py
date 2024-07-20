import funcoes
import interfaces as ifc
from dicionarios import clientes
from random import randint


def exibir_cliente(id_cliente):
    print()
    cliente = clientes[id_cliente][0]
    telefone = clientes[id_cliente][1]
    email = clientes[id_cliente][2]
    endereco = clientes[id_cliente][3]
    rua = endereco['rua']
    bairro = endereco['bairro']
    num_casa = endereco['num_casa']
    logradouro = f'R. {rua} {num_casa}, {bairro}'
    print()
    print(f'Nome: {cliente}')
    print(f'Telefone: {telefone}')
    print(f'Email: {email}')
    print(f'Cidade: {endereco["cidade"]}')
    print(f'Endereço: {logradouro}')
    print('Id de cadastro: ', id_cliente)
    print()


def cliente_indicio(codigo):
    if codigo in clientes:
        return False
    return True


def gerar_codigo_cliente():
    codigo = randint(0, 999999)
    
    codigo_formatado = f'{codigo:05d}'
    while not (cliente_indicio(codigo_formatado)):
        codigo = randint(0, 999999)
        codigo_formatado = f'{codigo:05d}'
    return codigo_formatado


def cadastrar_cliente():
    ifc.cabecalho_modulos('Cadastrar Cliente')
    nome_cliente = funcoes.ler_nome()
    telefone_cliente = funcoes.ler_telefone()
    email_cliente = funcoes.ler_email()
    cidade_cliente = funcoes.ler_cidade()
    bairro_cliente = funcoes.ler_logradouro('Bairro')
    rua_cliente = funcoes.ler_logradouro('Rua')
    num_casa_cliente = funcoes.ler_logradouro('Número da casa')

    id_cliente = gerar_codigo_cliente()
    clientes[id_cliente] = [
        nome_cliente,
        telefone_cliente,
        email_cliente,
        {
            'cidade': cidade_cliente,
            'bairro': bairro_cliente,
            'rua': rua_cliente,
            'num_casa': num_casa_cliente,
        },
    ]

    exibir_cliente(id_cliente)
    print('Cliente cadastrado com sucesso!')
    print()
    input('Tecle <ENTER> para continuar... ')


def pesquisar_cliente():
    ifc.cabecalho_modulos('Pesquisar Cliente')
    id_cliente = input('Qual o id do cliente? ')
    sair = 'n'
    while sair == 'n':    
        if id_cliente in clientes.keys():
            exibir_cliente(id_cliente)
        else:
            print('\nNão foi possível encontrar o cliente. Tem certeza que ele está cadastrado? ')
        
        sair = input('\nDeseja sair do módulo "Pesquisar Cliente" (S/N)? ').lower()
        print()
        if sair == "n":
            id_cliente = input('Qual o id do cliente? ')
    print()
    input('Tecle <ENTER> para continuar... ')


def atualizar_cliente():
    ifc.cabecalho_modulos('Atualizar Cliente')
    id_cliente = input('Qual o id do cliente? ')
    sair = 'n'
    while sair == 'n':
        if id_cliente in clientes.keys():
            nome_cliente = funcoes.ler_nome()
            telefone_cliente = funcoes.ler_telefone()
            email_cliente = funcoes.ler_email()
            cidade_cliente = funcoes.ler_cidade()
            bairro_cliente = funcoes.ler_logradouro('Nome do Bairro')
            rua_cliente = funcoes.ler_logradouro('Nome da Rua')
            num_casa_cliente = funcoes.ler_logradouro('Número da casa')

            clientes[id_cliente] = [
            nome_cliente,
            telefone_cliente,
            email_cliente,
            {
                'cidade': cidade_cliente,
                'bairro': bairro_cliente,
                'rua': rua_cliente,
                'num_casa': num_casa_cliente,
            },
        ]
            print('Novos dados do cliente: ')
            exibir_cliente(id_cliente)
            print('Dados do cliente atualizado com sucesso!')
        else:
            print('\nNão foi possível encontrar o cliente. Tem certeza que ele está cadastrado?')
        
        sair = input('\nDeseja sair do módulo "Pesquisar Cliente" (S/N)? ').lower()
        print()
        if sair == "n":
            id_cliente = input('Qual o id do cliente? ')
    print()
    input('Tecle <ENTER> para continuar... ')


def deletar_cliente():
    ifc.cabecalho_modulos('Deletar Cliente')
    id_cliente = input('Qual o id do cliente? ')
    print()

    if id_cliente in clientes.keys():
        exibir_cliente(id_cliente)

        resp = input('Tem certeza que deseja remover este cliente (S/N)? ').lower()

        if resp != 'n':
            del clientes[id_cliente]
            print('Cliente excluido com sucesso! ')
        else:
            print('Não foi possível excluir o cliente. ')
    else:
        print('Cliente não encontrado. Tem certeza que ele está cadastrado?')

    print()
    input('Tecle <ENTER> para continuar... ')
