import re
import pickle
import interfaces as ifc
from random import randint
from validacoes import validacoes
from dicionarios import clientes, produtos, vendas, formas_pagamento


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
    print()
    nome = input("››››› Nome: ")
    while not validacoes.validar_nome(nome):
        print('\033[91m')
        print("»› Ops! Algo deu errado! \n»› Digite apenas letras. Tente novamente...")
        print('\033[0m')
        
        nome = input("››››› Nome: ")
    nome = nome.strip().title()
    nome = re.sub(r"\s+", " ", nome)
    return nome


def ler_nome_regex():
    print()
    nome = input("››››› Nome: ")
    while not validacoes.validar_nome_regex(nome):
        print('\033[91m')
        print("»› Ops! Algo deu errado! \n»› Digite apenas letras. Tente novamente...")
        print('\033[0m')
        
        nome = input("››››› Nome: ")
    return nome


def ler_telefone():
    print()
    tel = input("››››› Telefone (somente números): ")
    while not (validacoes.validar_telefone(tel)):
        print('\033[91m')
        print("»› Ops! Algo deu errado! \n»› Digite apenas números. Tente novamente...")
        print('\033[0m')
        
        tel = input("››››› Telefone (somente números): ")
    return tel


def ler_email():
    print()
    email = input("››››› Email: ")
    while not (validacoes.validar_email(email)):
        print('\033[91m')
        print("»› Ops! Algo deu errado! \n»› Digite um email válido. Tente novamente...")
        print('\033[0m')
        
        email = input("››››› Email: ")
    return email


def ler_quantidade():
    print()
    qtd = input("››››› Quantidade (somente números): ")
    while not validacoes.validar_quantidade(qtd):
        print('\033[91m')
        print("»› Ops! Algo deu errado! \n»› Digite apenas números. Tente novamente...")
        print('\033[0m')
        
        qtd = input("››››› Quantidade (somente números): ")
    return qtd


def ler_preco():
    print()
    preco = input("››››› Preço da Unidade (00,00): ")
    while not validacoes.validar_preco(preco):
        print('\033[91m')
        print("»› Ops! Algo deu errado! \n»› Siga o padrão (00,00). Tente novamente...")
        print('\033[0m')
        
        preco = input("››››› Preço da Unidade (00,00): ")
    preco = preco.replace(",", ".")
    return preco


def ler_cidade():
    print()
    cidade = input("››››› Cidade (inclua os acentos): ").upper()
    while not validacoes.validar_cidade(cidade):
        print('\033[91m')
        print("»› Ops! Essa cidade não existe no Brasil. \n»› Lembre de incluir os acentos. Tente novamente...")
        print('\033[0m')
        
        cidade = input("››››› Cidade (inclua os acentos): ").upper()
    return cidade


def ler_logradouro(parte):
    print()
    logra = input(f"››››› {parte}: ")
    while not validacoes.validar_logradouro(logra):
        print('\033[91m')
        print('»› Ops! Algo deu errado! \n»› Digite apenas letras, números e "-". Tente novamente...')
        print('\033[0m')
        
        logra = input(f"››››› {parte}: ")
    logra = logra.strip().title()
    logra = re.sub(r"\s+", " ", logra)
    return logra


def ler_codigo(texto, dicio):
    print()
    codigo = input(f"››››› {texto}")
    while not validacoes.validar_codigo(dicio, codigo):
        print('\033[91m')
        print("»› Ops! Algo deu errado! \n»› Tem certeza que este é código certo? Tente novamente...")
        print('\033[0m')
        
        codigo = input(f"››››› {texto}")
    return codigo


def ler_form_pag():
    print()
    forma_pagamento = input("››››› Forma de pagamento: \n››››› 1 - Cartão de Débito \n››››› 2 - Cartão de Crédito \n››››› 3 - Espécie \n››››› 4 - PIX \n: ")
    
    while not validacoes.validar_codigo(formas_pagamento, forma_pagamento):
        print('\033[91m')
        print("»› Ops! Algo deu errado! \n»› Escolha uma forma de pagamento válida. Tente novamente...")
        print('\033[0m')
        
        forma_pagamento = input("››››› Forma de pagamento: \n››››› 1 - Cartão de Débito \n››››› 2 - Cartão de Crédito \n››››› 3 - Espécie \n››››› 4 - PIX \n: ")
        
    return forma_pagamento


#########################
#####     MENUS     #####
#########################
def menu_principal():
    ifc.interface_menu_principal()
    op_mprinc = input("››››› Escolha sua opção: ")
    return op_mprinc


##### MÓDULO CADASTRAR #####
def menu_cadastrar():
    ifc.interface_menu_cadastrar()
    op_mcadas = input("››››› Escolha sua opção: ")
    return op_mcadas


##### MÓDULO PESQUISAR #####
def menu_pesquisar():
    ifc.interface_menu_pesquisar()
    op_mpesq = input("››››› Escolha sua opção: ")
    return op_mpesq


##### MÓDULO ATUALIZAR #####
def menu_atualizar():
    ifc.interface_menu_atualizar()
    op_matua = input("››››› Escolha sua opção: ")
    return op_matua


##### MÓDULO DELETAR #####
def menu_deletar():
    ifc.interface_menu_deletar()
    op_mdele = input("››››› Escolha sua opção: ")
    return op_mdele


##### MÓDULO RELATÓRIO #####
def menu_relatorio():
    ifc.interface_menu_relatorio()
    op_mrela = input("››››› Escolha sua opção: ")
    return op_mrela


##### MÓDULO INFORMAÇÕES #####
def informacoes():
    ifc.interface_informacoes()
    input("»› Tecle <ENTER> para continuar... ")


##############################
#####         ÚTIL       #####
##############################


#####      TRUNCATE      #####
# ChatGPT
def truncate_string(s, length):
    if len(s) > length:
        return s[: length - 3] + "..."
    return s


##### CHECAR DE CÓDIGO #####
def codigo_indicio(codigo, dicio):
    if codigo in dicio:
        return False
    return True


##### GERAR DE CÓDIGO #####
def gerar_codigo(dicio):
    codigo = randint(0, 999999)

    codigo_formatado = f"{codigo:06d}"
    while not (codigo_indicio(codigo_formatado, dicio)):
        codigo = randint(0, 999999)
        codigo_formatado = f"{codigo:06d}"
    return codigo_formatado


##### PESQUISAR CLIENTE POR NOME #####
def pesquisar_nome_cliente():
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
                    
                    cidade = truncate_string(endereco['cidade'], 22)
                    logradouro = truncate_string(f'R. {rua} {num_casa}, {bairro}', 27)
                    nome_cliente = truncate_string(clientes[c][0], 26)
                    email_cliente = truncate_string(clientes[c][2], 26)
                    
                    print('| %-8s ' % (c), end='')
                    print('| %-27s ' % (nome_cliente), end='')
                    print('| %-15s ' % (tel), end='')
                    print('| %-26s ' % (email_cliente), end='')
                    print('| %-29s ' % (logradouro), end='')
                    print('| %-22s |' % (cidade))
            print('|══════════|═════════════════════════════|═════════════════|════════════════════════════|═══════════════════════════════|════════════════════════|')


##### PESQUISAR PRODUTO POR NOME #####
def pesquisar_nome_produto():
    nome_prod = input('Digite o nome do produto: ').lower()
    lista_nomes = []
    
    for codigo in produtos:
        nome_produto = produtos[codigo][0].lower()
        # print(nome_produto)
        if nome_prod in nome_produto:
            lista_nomes.append(nome_produto)
    # print(lista_nomes)
    if not lista_nomes:
        print('\nNÃO HÁ PRODUTOS COM ESSE NOME\n')
    else:
        ifc.interface_pesquisar_produtos()
        for nome in lista_nomes:
            for p in produtos:
                if nome.lower() == produtos[p][0].lower():
                    nome_produto = truncate_string(produtos[p][0], 26)
                    print('| %-8s ' % (p), end='')
                    print('| %-27s ' % (nome_produto), end='')
                    print('| %-18s ' % (produtos[p][1]), end='')
                    print('| %-15s |' % (produtos[p][2]))
            print('|══════════|═════════════════════════════|════════════════════|═════════════════|')


##### CHECAR NOME #####
def nome_indicio(nome, dicio):
    nomes_dicio = []
    for cod in dicio:
        nomes_dicio.append(dicio[cod][0].lower())
    
    if nome.lower() not in nomes_dicio:
        return False
    return True

##### NOME → CÓDIGO #####
def nome_pra_codigo(nome, dicio):
    codigo = ''
    for cod in dicio:
        # print(cod)
        if nome.lower() == dicio[cod][0].lower():
            codigo = cod
            # print(codigo)
    return codigo