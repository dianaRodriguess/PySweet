vendas = {
    "112233": [
        {
            "000000": ["quant_produto0", "preco_produto0"],
            "111100": ["quant_produto1", "preco_produto1"],
            "222200": ["quant_produto2", "preco_produto2"],
            "333300": ["quant_produt03", "preco_produto3"],
        },
        "id_cliete",
        "quantidade_total",
        "preco_total",
        "forma_pag",
        "data",
    ],
    "223344": [
        {
            "000011": ["quant_produto0", "preco_produto0"],
            "111111": ["quant_produto1", "preco_produto1"],
            "222211": ["quant_produto2", "preco_produto2"],
            "333311": ["quant_produt03", "preco_produto3"],
        },
        "id_cliete1",
        "quantidade_total1",
        "preco_total1",
        "forma_pag1",
        "data1",
    ],
    "334455": [
        {
            "000022": ["quant_produto0", "preco_produto0"],
            "111122": ["quant_produto1", "preco_produto1"],
            "222222": ["quant_produto2", "preco_produto2"],
            "333322": ["quant_produt03", "preco_produto3"],
        },
        "id_cliete2",
        "quantidade_total3",
        "preco_total4",
        "forma_pag5",
        "data4",
    ]
}
print('|--------------------------------------------------------------------------------------------------------------------------------------|')
print('|------------------------------------------♥ ♥ ♥ ♥ ♥ ♥ ♥ Ver todas as vendas ♥ ♥ ♥ ♥ ♥ ♥ ♥---------------------------------------------|')
print('|--------------------------------------------------------------------------------------------------------------------------------------|')
print('|══════════|════════════════════════════|═══════════════|══════════════════|════════════|════════════════════|')
print('|    ID    |          Comprador         |  Qtd.vendida  |  Form.Pagamento  |  Valor R$  |        Data        |')
print('|══════════|════════════════════════════|═══════════════|══════════════════|════════════|════════════════════|')
for ids, details in vendas.items():
    produtos_dicio = list
    print(produtos_dicio)
    # for codigo, infor in produtos.items():
    #     print(f"Produto: {codigo}", end="")
    #     print(f"\tQuantidade: {infor[0]}", end="")
    #     print(f"\tPreço: {infor[1]}")

    # print(f"ID {details[1]}")
    # print(f"Quantidade total {details[1]}")
    # print(f"Preço total {details[1]}")
    # print(f"Forma de pagamento {details[1]}")
    # print(f"Data {details[1]}")
    print('|══════════|════════════════════════════|═════════════════════════|═══════════════|══════════════════|════════════|════════════════════|')
input("Tecle <ENTER> para continuar... ")
