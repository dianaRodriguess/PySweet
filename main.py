from cliente import cadastrarCliente, pesquisarCliente, atualizarCliente, deletarCliente
from funcoes import (
    atualizarProduto,
    atualizarVenda,
    deletarProduto,
    deletarVenda,
    informacoes,
    maioresCompradores,
    menuPrincipal,
    menuCadastrar,
    menuAtualizar,
    menuPesquisar,
    menuDeletar,
    menuRelatorio,
    cadastrarVenda,
    cadastrarProduto,
    pesquisarProduto,
    pesquisarVenda,
    exibirClientes,
    exibirProdutos,
    exibirVendas,
    prdtMaisVend,
    escreverArquivos
)

######################################
#####      Projeto PySweet       #####
######################################

# MENU PRINCIPAL
op_mprinc = ""
while op_mprinc != "0":
    op_mprinc = menuPrincipal()

    # MÓDULO CADASTRAR
    if op_mprinc == "1":
        op_mcadas = ""
        while op_mcadas != "0":
            op_mcadas = menuCadastrar()
            print()

            if op_mcadas == "1":
                cadastrarCliente()
            elif op_mcadas == "2":
                cadastrarVenda()
            elif op_mcadas == "3":
                cadastrarProduto()
    # MÓDULO PESQUISAR
    elif op_mprinc == "2":
        op_mpesq = ""
        while op_mpesq != "0":
            op_mpesq = menuPesquisar()
            print()

            if op_mpesq == "1":
                pesquisarCliente()
            elif op_mpesq == "2":
                pesquisarVenda()
            elif op_mpesq == "3":
                pesquisarProduto()
    # MÓDULO ATUALIZAR
    elif op_mprinc == "3":
        op_matua = ""
        while op_matua != "0":
            op_matua = menuAtualizar()
            print()

            if op_matua == "1":
                atualizarCliente()
            elif op_matua == "2":
                atualizarVenda()
            elif op_matua == "3":
                atualizarProduto()
    # MÓDULO DELETAR
    elif op_mprinc == "4":
        op_mdele = ""
        while op_mdele != "0":
            op_mdele = menuDeletar()
            print()

            if op_mdele == "1":
                deletarCliente()
            elif op_mdele == "2":
                deletarVenda()
            elif op_mdele == "3":
                deletarProduto()
    # MÓDULO RELATÓRIO
    elif op_mprinc == "5":
        op_mrela = ""
        while op_mrela != "0":
            op_mrela = menuRelatorio()
            print()

            if op_mrela == "1":
                exibirClientes()
            elif op_mrela == "2":
                exibirVendas()
            elif op_mrela == "3":
                exibirProdutos()
            elif op_mrela == "4":
                prdtMaisVend()
            elif op_mrela == "5":
                maioresCompradores()
            # elif op_mrela == "6":
            #     dtMaisVendem()
    # MÓDULO INFORMAÇÕES
    elif op_mprinc == "6":
        informacoes()

print()
print("Você encerrou o programa!")
print("Até logo!")

# função ler o dicio e  escreve nos arquivos
escreverArquivos()