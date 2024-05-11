import pickle

"""
clientes - nome, telefone, email, endereço
produtos - nome, quantidade, preço
vendas - cliente, produto, qtdvendida, data, fdp
"""

clientes = {"1": ["Cliente Teste", "00000", "teste@teste.com", "Rua Teste"]}
produtos = {"1": ["Produto Teste", "9999", "0.50"]}
vendas = {"1": ["1", "1", "999", "00/00/0000", "PIX"]}

# escrever o dicionário no arquivo
try:
    arq_clientes = open("clientes.dat", "rb")
    clientes = pickle.load(arq_clientes)
except:
    arq_clientes = open("clientes.dat", "wb")
arq_clientes.close()

try:
    arq_produtos = open("produtos.dat", "rb")
    produtos = pickle.load(arq_produtos)
except:
    arq_produtos = open("produtos.dat", "wb")
arq_produtos.close()

try:
    arq_vendas = open("vendas.dat", "rb")
    vendas = pickle.load(arq_vendas)
except:
    arq_vendas = open("vendas.dat", "wb")
arq_vendas.close()