import csv
import json

# 1. Abrir e ler o arquivo JSON com as metas da empresa
with open("configuracao.json", "r", encoding="utf-8") as arquivo_json:
    config = json.load(arquivo_json)

empresa = config["empresa"]
periodo = config["periodo"]
meta = config["meta_faturamento"]
orcamento = config["orcamento_despesas"]

# 2. Preparar variáveis para guardar os totais
faturamento_total = 0
unidades_totais = 0
numero_registros = 0
quantidade_por_produto = {}  # Dicionário para somar as unidades de cada produto

# 3. Abrir e ler o arquivo CSV com as vendas
with open("vendas.csv", "r", encoding="utf-8") as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter=";")
    next(leitor)  # Pula a primeira linha (cabeçalho: data;produto;quantidade;preco_unitario)

    for linha in leitor:
        # Cada linha é uma lista: [0]=data, [1]=produto, [2]=quantidade, [3]=preco_unitario
        produto = linha[1]
        quantidade = int(linha[2])
        preco = float(linha[3])

        # Calcular o valor total desta venda e atualizar os totais gerais
        valor_venda = quantidade * preco
        faturamento_total = faturamento_total + valor_venda
        unidades_totais = unidades_totais + quantidade
        numero_registros = numero_registros + 1

        # Somar a quantidade vendida por produto usando if/else tradicional
        if produto in quantidade_por_produto:
            quantidade_por_produto[produto] = quantidade_por_produto[produto] + quantidade
        else:
            quantidade_por_produto[produto] = quantidade

# 4. Calcular a média por venda
media_por_venda = faturamento_total / numero_registros

# 5. Descobrir qual produto teve a maior quantidade vendida (usando for e if)
produto_mais_vendido = ""
maior_quantidade = 0

for produto, qtd in quantidade_por_produto.items():
    if qtd > maior_quantidade:
        maior_quantidade = qtd
        produto_mais_vendido = produto

# 6. Apresentar o relatório final para a administração
print("=" * 50)
print(f"RELATÓRIO DE VENDAS - {empresa}")
print(f"Período: {periodo}")
print("=" * 50)
print(f"Número de registros de venda: {numero_registros}")
print(f"Total de unidades vendidas: {unidades_totais}")
print(f"Faturamento total: R$ {faturamento_total:.2f}")
print(f"Valor médio por venda: R$ {media_por_venda:.2f}")
print()

print("Quantidade vendida por produto:")
for produto, qtd in quantidade_por_produto.items():
    print(f" - {produto}: {qtd} unidades")

print()
print(f"Produto mais vendido: {produto_mais_vendido} ({maior_quantidade} unidades)")
print()

# 7. Comparar o faturamento com a meta e com o orçamento
print(f"Meta de faturamento: R$ {meta:.2f}")
if faturamento_total >= meta:
    sobra_meta = faturamento_total - meta
    percentual = (faturamento_total / meta) * 100
    print(f"A meta foi ATINGIDA! Passamos R$ {sobra_meta:.2f} da meta ({percentual:.1f}% do objetivo).")
else:
    falta_meta = meta - faturamento_total
    percentual = (faturamento_total / meta) * 100
    print(f"A meta NÃO foi atingida. Faltaram R$ {falta_meta:.2f} ({percentual:.1f}% do objetivo).")

print()
print(f"Orçamento previsto para despesas: R$ {orcamento:.2f}")
if faturamento_total >= orcamento:
    lucro_bruto = faturamento_total - orcamento
    print(f"O faturamento cobre as despesas, com sobra de R$ {lucro_bruto:.2f}.")
else:
    prejuizo = orcamento - faturamento_total
    print(f"Atenção: o faturamento não cobre as despesas (faltam R$ {prejuizo:.2f}).")
print("=" * 50)


