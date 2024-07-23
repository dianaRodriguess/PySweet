import pickle

"""
clientes = [nome, telefone, email, 
{'rua': 'nome da rua', 
'num_casa': '10A',
'bairro': 'nome do bairro',
'cidade': 'nome da cidade',
}]
produtos - [nome, quantidade, preço]
vendas -  id_produto, id_cliente, qtdvendida, forma_pagamento, valor, data
"""

clientes = {
    "000000": [
        "Cliente Fixo",
        "84901234567",
        "cliente@fixo.com",
        {
            "rua": "Rua Fixa",
            "bairro": "Bairro fixo",
            "num_casa": "10F",
            "cidade": "Fixada",
        },
    ]
}

produtos = {"000000": ["Produto Fixo", "1000", "1.50"]}
vendas = {"000000": [{"000000": ['10', '15.00']}, "000000", "10", "1", "15.00", "01/01/01, 00:00:00"]}

formas_pagamento = {
    "1": "Cartão de Credito",
    "2": "Cartão de Débito",
    "3": "Especie",
    "4": "Pix",
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
