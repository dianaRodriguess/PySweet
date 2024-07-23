from cruds import cliente
from cruds import venda
from cruds import produto
import relatorios
import funcoes

######################################
#####      Projeto PySweet       #####
######################################

# MENU PRINCIPAL
op_mprinc = ''
while op_mprinc != '0':
    op_mprinc = funcoes.menu_principal()
    match op_mprinc:
        case '1':  # MÓDULO CADASTRAR
            op_mcadas = ''
            while op_mcadas != '0':
                op_mcadas = funcoes.menu_cadastrar()
                print()
                match op_mcadas:
                    case '1':
                        cliente.cadastrar_cliente()
                    case '2':
                        venda.cadastrar_venda()
                    case '3':
                        produto.cadastrar_produto()
        case '2':  # MÓDULO PESQUISAR
            op_mpesq = ''
            while op_mpesq != '0':
                op_mpesq = funcoes.menu_pesquisar()
                print()
                match op_mpesq:
                    case '1':
                        cliente.pesquisar_cliente()
                    case '2':
                        venda.pesquisar_venda()
                    case '3':
                        produto.pesquisar_produto()
        case '3':  # MÓDULO ATUALIZAR
            op_matua = ''
            while op_matua != '0':
                op_matua = funcoes.menu_atualizar()
                print()
                match op_matua:
                    case '1':
                        cliente.atualizar_cliente()
                    case '2':
                        venda.atualizar_venda()
                    case '3':
                        produto.atualizar_produto()
        case '4':  # MÓDULO DELETAR
            op_mdele = ''
            while op_mdele != '0':
                op_mdele = funcoes.menu_deletar()
                print()
                match op_mdele:
                    case '1':
                        cliente.deletar_cliente()
                    case '2':
                        venda.deletar_venda()
                    case '3':
                        produto.deletar_produto()
        case '5':  # MÓDULO RELATÓRIO
            op_mrela = ''
            while op_mrela != '0':
                op_mrela = funcoes.menu_relatorio()
                print()
                match op_mrela:
                    case '1':
                        relatorios.ver_clientes()
                    case '2':
                        relatorios.ver_vendas()
                    case '3':
                        relatorios.ver_produtos()
                    case '4':
                        relatorios.prdt_mais_vend()
                    case '5':
                        relatorios.maiores_compradores()
                    case '6':
                        relatorios.checar_estoque()
        case '6':  # MÓDULO INFORMAÇOES
            funcoes.informacoes()

print()
print('‹♥› Você encerrou o programa! ‹♥›')
print('‹♥› Até logo! ‹♥›')

# função ler o dicio e  escreve nos arquivos
funcoes.escrever_arquivos()
