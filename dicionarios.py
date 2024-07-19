import pickle

"""
clientes - nome, telefone, email, endereço
produtos - nome, quantidade, preço
vendas -  id_produto, id_cliente, qtdvendida, forma_pagamento, valor, data
"""

clientes = {"1": ["Cliente Teste", "00000", "teste@teste.com", "Rua Teste"]}
produtos = {"1": ["Produto Teste", "9999", "0.50"]}
vendas = {"1": ["1", "1", "100", 1, "0.50", "01/01/01, 00:00:00"]}

formas_pagamento = {
    1: "Cartão de Credito",
    2: "Cartão de Débito",
    3: "Especie",
    4: "Pix",
}

# escrever o dicionário no arquivo
try:
    arq_clientes = open("data/clientes.dat", "rb")
    clientes = pickle.load(arq_clientes)
except:
    arq_clientes = open("data/clientes.dat", "wb")
arq_clientes.close()

try:
    arq_produtos = open("data/produtos.dat", "rb")
    produtos = pickle.load(arq_produtos)
except:
    arq_produtos = open("data/produtos.dat", "wb")
arq_produtos.close()

try:
    arq_vendas = open("data/vendas.dat", "rb")
    vendas = pickle.load(arq_vendas)
except:
    arq_vendas = open("data/vendas.dat", "wb")
arq_vendas.close()
