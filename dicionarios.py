import json

"""
clientes - nome, telefone, email, endereço
produtos - nome, quantidade, preço
vendas - cliente, produto, qtdvendida, data, fdp
"""

clientes = {"1": ["Cliente Teste", "00000", "teste@teste.com", "Rua Teste"]}
produtos = {"1": ["Produto Teste", "9999", "0.50"]}
# mudar vendas id cliente e id produto
vendas = {"1": ["Cliente Teste", "Produto Teste", "999", "00/00/0000", "PIX"]}


# with open("clientes.json", "w") as file:
#     json.dump(clientes, file)

# with open("produtos.json", "w") as file:
#     json.dump(produtos, file)

# with open("vendas.json", "w") as file:
#     json.dump(vendas, file)


# aqui