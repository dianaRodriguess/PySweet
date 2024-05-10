import json
import pickle

"""
clientes - nome, telefone, email, endereço
produtos - nome, quantidade, preço
vendas - cliente, produto, qtdvendida, data, fdp
"""

clientes = {"1": ["Cliente Teste", "00000", "teste@teste.com", "Rua Teste"]}
produtos = {"1": ["Produto Teste", "9999", "0.50"]}
# mudar vendas id cliente e id produto
vendas = {"1": ["Produto Teste", "Cliente Teste", "999", "00/00/0000", "PIX"]}


# with open("clientes.json", "w") as file:
#     json.dump(clientes, file)

# with open("produtos.json", "w") as file:
#     json.dump(produtos, file)

# with open("vendas.json", "w") as file:
#     json.dump(vendas, file)


# aqui

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