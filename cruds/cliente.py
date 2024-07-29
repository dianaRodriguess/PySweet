import funcoes
import interfaces as ifc
from dicionarios import clientes


def exibir_cliente(id_cliente):
    print()
    cliente = clientes[id_cliente][0]
    telefone = clientes[id_cliente][1]
    tel = f'({telefone[0:2]}) {telefone[2:7]}-{telefone[7:]}'
    email = clientes[id_cliente][2]
    endereco = clientes[id_cliente][3]
    rua = endereco["rua"]
    bairro = endereco["bairro"]
    num_casa = endereco["num_casa"]
    logradouro = f"R. {rua} {num_casa}, {bairro}"
    print('‹♥› Informações do Cliente ‹♥›')
    print(f"»› Nome: {cliente}")
    print(f"»› Telefone: {tel}")
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
    print('\033[92m')
    print("»› Cliente cadastrado com sucesso!")
    print('\033[0m')

    input("»› Tecle <ENTER> para continuar... ")


def pesquisar_cliente():
    ifc.cabecalho_modulos("Pesquisar Cliente")
    
    nome_cli = input('Digite o nome do cliente: ').lower()
    lista_nomes = []
        
    for codigo in clientes:
        nome_cliente = clientes[codigo][0].lower()
        if nome_cli in nome_cliente:
            lista_nomes.append(nome_cliente)  # se nome_cliente tem nome_cli, lista_nomes ganha nome_cliente 
            
    if not lista_nomes:  # se não há nada em lista_nomes, print ↓
        print('\nNÃO HÁ CLIENTES COM ESSE NOME\n')
    else:  # se tiver algo em lista_nomes
        ifc.interface_pesquisar_clientes()
        for nome in lista_nomes:
            for c in clientes:
                if nome.lower() == clientes[c][0].lower():  # compara o nome da lista com o nome guardado
                    telefone = clientes[c][1]
                    tel = f'({telefone[0:2]}) {telefone[2:7]}-{telefone[7:]}'
                    endereco = clientes[c][3]
                    rua = endereco['rua']
                    bairro = endereco['bairro']
                    num_casa = endereco['num_casa']
                    
                    cidade = funcoes.truncate_string(endereco['cidade'], 22)
                    logradouro = funcoes.truncate_string(f'R. {rua} {num_casa}, {bairro}', 27)
                    nome_cliente = funcoes.truncate_string(clientes[c][0], 26)
                    email_cliente = funcoes.truncate_string(clientes[c][2], 26)
                    
                    print('| %-8s ' % (c), end='')
                    print('| %-27s ' % (nome_cliente), end='')
                    print('| %-15s ' % (tel), end='')
                    print('| %-26s ' % (email_cliente), end='')
                    print('| %-29s ' % (logradouro), end='')
                    print('| %-22s |' % (cidade))
            print('|══════════|═════════════════════════════|═════════════════|════════════════════════════|═══════════════════════════════|════════════════════════|')
        # Tem que ser dentro do else
        detalhe = input('Quer informações detalhadas de um cliente (S/N)? ').lower()
        if detalhe == 's':
            id_cliente = funcoes.ler_codigo('Digite o ID de cadastro do cliente: ', clientes)
            exibir_cliente(id_cliente)
    
    input("\n»› Tecle <ENTER> para continuar... ")


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
        print("‹♥› Novos dados do cliente ‹♥›")
        exibir_cliente(id_cliente)
        print('\033[92m')
        print("»› Dados do cliente atualizados com sucesso!")
        print('\033[0m')

        sair = input('»› Deseja sair do módulo "Atualizar Cliente" (S/N)? ').lower()
        print()
        if sair == "n":
            id_cliente = funcoes.ler_codigo('Digite o ID de cadastro do cliente: ', clientes)

    input("»› Tecle <ENTER> para continuar... ")


def deletar_cliente():
    ifc.cabecalho_modulos("Deletar Cliente")
    id_cliente = funcoes.ler_codigo('Digite o ID de cadastro do cliente: ', clientes)
    sair = "n"
    while sair == "n":
        exibir_cliente(id_cliente)
        print('\033[33m')
        resp = input("»› Tem certeza que deseja deletar este cliente (S/N)? ").lower()
        print('\033[0m')
        if resp == "s":
            del clientes[id_cliente]
            print('\033[92m')
            print("»› Cliente deletado com sucesso! ")
            print('\033[0m')
        else:
            print('\033[91m')
            print("»› Não foi possível deletar o cliente. ")
            print('\033[0m')

        sair = input('»› Deseja sair do módulo "Deletar Cliente" (S/N)? ').lower()
        print()
        if sair == "n":
            id_cliente = funcoes.ler_codigo('Digite o ID de cadastro do cliente: ', clientes)

    input("»› Tecle <ENTER> para continuar... ")
