import cliente
import venda
import produto
import relatorios
import funcoes

######################################
#####      Projeto PySweet       #####
######################################

# MENU PRINCIPAL
op_mprinc = ""
while op_mprinc != "0":
    op_mprinc = funcoes.menuPrincipal()
    match op_mprinc:
        case "1": # MÓDULO CADASTRAR
            op_mcadas = ""
            while op_mcadas != "0":
                op_mcadas = funcoes.menuCadastrar()
                print()
                match op_mcadas:
                    case "1":
                        cliente.cadastrarCliente()
                    case "2":
                        venda.cadastrarVenda()
                    case "3":
                        produto.cadastrarProduto()
        case "2": # MÓDULO PESQUISAR
            op_mpesq = ""
            while op_mpesq != "0":
                op_mpesq = funcoes.menuPesquisar()
                print()
                match op_mpesq:
                    case "1":
                        cliente.pesquisarCliente()
                    case "2":
                        venda.pesquisarVenda()
                    case "3":
                        produto.pesquisarProduto()
        case "3": # MÓDULO ATUALIZAR
            op_matua = ""
            while op_matua != "0":
                op_matua = funcoes.menuAtualizar()
                print()
                match op_matua:
                    case "1":
                        cliente.atualizarCliente()
                    case "2":
                        venda.atualizarVenda()
                    case "3":
                        produto.atualizarProduto()
        case "4": # MÓDULO DELETAR
            op_mdele = ""
            while op_mdele != "0":
                op_mdele = funcoes.menuDeletar()
                print()
                match op_mdele:
                    case "1":
                        cliente.deletarCliente()
                    case "2":
                        venda.deletarVenda()
                    case "3":
                        produto.deletarProduto()
        case "5": # MÓDULO RELATÓRIO
            op_mrela = ""
            while op_mrela != "0":
                op_mrela = funcoes.menuRelatorio()
                print()
                match op_mrela:
                    case "1":
                        relatorios.exibirClientes()
                    case "2":
                        relatorios.exibirVendas()
                    case "3":
                        relatorios.exibirProdutos()
                    case "4":
                        relatorios.prdtMaisVend()
                    case "5":
                        relatorios.maioresCompradores()
        case "6": # MÓDULO INFORMAÇOES
            funcoes.informacoes()

print()
print("Você encerrou o programa!")
print("Até logo!")

# função ler o dicio e  escreve nos arquivos
funcoes.escreverArquivos()
