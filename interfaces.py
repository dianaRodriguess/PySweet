import os

##############################
##### INTERFACES DE MENU #####
##############################


def interface_menu_principal():
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


def interface_menu_cadastrar():
    os.system("clear")
    print("############################################")
    print("#####         Módulo Cadastrar          ####")
    print("############################################")
    print("#####   1 - Cadastrar Cliente          #####")
    print("#####   2 - Cadastrar Venda            #####")
    print("#####   3 - Cadastrar Produto          #####")
    print("#####   0 - Sair                       #####")
    print()


def interface_menu_pesquisar():
    os.system("clear")
    print("############################################")
    print("#####          Módulo Pesquisar         ####")
    print("############################################")
    print("#####   1 - Pesquisar Cliente          #####")
    print("#####   2 - Pesquisar Venda            #####")
    print("#####   3 - Pesquisar Produto          #####")
    print("#####   0 - Sair                       #####")
    print()


def interface_menu_atualizar():
    os.system("clear")
    print("############################################")
    print("#####         Módulo Atualizar          ####")
    print("############################################")
    print("#####   1 - Atualizar Cliente          #####")
    print("#####   2 - Atualizar Venda            #####")
    print("#####   3 - Atualizar Produto          #####")
    print("#####   0 - Sair                       #####")
    print()


def interface_menu_deletar():
    os.system("clear")
    print("############################################")
    print("#####           Módulo Deletar          ####")
    print("############################################")
    print("#####   1 - Deletar Cliente            #####")
    print("#####   2 - Deletar Venda              #####")
    print("#####   3 - Deletar Produto            #####")
    print("#####   0 - Sair                       #####")
    print()


def interface_menu_relatorio():
    os.system("clear")
    print("############################################")
    print("#####   Você está no Módulo Relatório   ####")
    print("############################################")
    print("#####   1 - Exibir todos os clientes   #####")
    print("#####   2 - Exibir todos os vendas     #####")
    print("#####   3 - Exibir todas as produtos   #####")
    print("#####   4 - Produtos com mais vendem   #####")
    print("#####   5 - Maiores compradores        #####")
    print("#####   6 - Datas que mais vendem      #####")
    print("#####   0 - Sair                       #####")
    print()


def interface_informacoes():
    os.system("clear")
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


###################################
##### INTERFACES DE CABEÇALHO #####
###################################
def cabecalho_modulos(titulo):
    os.system("clear")
    titulo_len = len(titulo)
    total_length = titulo_len + 10
    margem = (total_length - titulo_len - 4) // 2  # 4 espaços para "####"
    linha_titulo = "#" * 5 + " " * margem + titulo + " " * margem + "#" * 5
    linha = "#" * total_length + "#" * 6
    print(linha)
    print(linha_titulo)
    print(linha)
    print()


def interface_ver_clientes():
    os.system("clear")
    print(
        "####################################################################################################################"
    )
    print(
        "#################################             Exibir todos os clientes            ##################################"
    )
    print(
        "####################################################################################################################"
    )
    print(
        "|------|-----------------------------|--------------------|----------------------------|---------------------------|"
    )
    print(
        "|  Id  |        Nome Completo        |      Telefone      |            Email           |          Endereço         |"
    )
    print(
        "|------|-----------------------------|--------------------|----------------------------|---------------------------|"
    )


def interface_ver_vendas():
    os.system("clear")
    print(
        "####################################################################################################################################"
    )
    print(
        "#########################################             Exibir todas as vendas             ###########################################"
    )
    print(
        "####################################################################################################################################"
    )
    print(
        "|------|----------------------------|-------------------------|---------------|------------------|------------|--------------------|"
    )
    print(
        "|  Id  |          Comprador         |         Produto         |  Qtd.vendida  |  Form.Pagamento  |    Valor   |        Data        |"
    )
    print(
        "|------|----------------------------|-------------------------|---------------|------------------|------------|--------------------|"
    )


def interface_ver_produtos():
    os.system("clear")
    print(
        "#############################################################################"
    )
    print(
        "###################        Exibir todos os produtos        ##################"
    )
    print(
        "#############################################################################"
    )
    print(
        "|------|-----------------------------|--------------------|-----------------|"
    )
    print(
        "|  Id  |           Produto           |     Quantidade     |    Preço (R$)   |"
    )
    print(
        "|------|-----------------------------|--------------------|-----------------|"
    )


def interface_prdt_mais_vend():  # produtos mais vendidos
    os.system("clear")
    print("####################################################")
    print("##########      Produtos Mais Vendidos     #########")
    print("####################################################")
    print("|-----------------------------|--------------------|")
    print("|           Produto           |     Quantidade     |")
    print("|-----------------------------|--------------------|")


def interface_maiores_compradores():
    os.system("clear")
    print("####################################################")
    print("###########      Maiores Compradores      ##########")
    print("####################################################")
    print("|-----------------------------|--------------------|")
    print("|           Cliente           |     Quantidade     |")
    print("|-----------------------------|--------------------|")
