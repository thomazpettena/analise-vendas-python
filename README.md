# Análise de vendas - Academia Allure Fitness

## Contexto da empresa
A Academia Allure Fitness é uma academia fictícia, inspirada em uma academia de Campinas. Ela vende mensalidades, planos, treinos avulsos, avaliações físicas e diárias de personal trainer. A administração precisa decidir o que fazer no próximo mês, baseando-se nos ultuimos 10 dias de outubro, mas as informações estão em arquivos separados: as vendas e as metas. O programa junta os dois e gera um resumo.

## Arquivos do projeto
- `vendas.csv`: 12 registros de vendas de outubro de 2026 (data, produto, quantidade e preço unitário).
- `configuracao.json`: nome da empresa, período, meta de faturamento, orçamento de despesas e categorias.
- `analise.py`: programa em Python que lê os dois arquivos e faz os cálculos.
- `README.md`: este arquivo.

## Como o programa funciona
1. Lê o `configuracao.json` com o módulo `json`.
2. Lê o `vendas.csv` com o módulo `csv`.
3. Calcula o valor de cada venda (quantidade x preço unitário).
4. Calcula o faturamento total, o total de unidades e o número de registros.
5. Descobre o produto mais vendido.
6. Compara o faturamento com a meta e com o orçamento de despesas.
7. Mostra o resumo na tela.

## Como executar
1. Instale o Python 3.
2. Deixe os 3 arquivos na mesma pasta.
3. No terminal, dentro da pasta, rode: `analise.py`

## Integrantes e contribuições
- Thomaz Pettená: Eu pensei em uma academia que existe na vida real, a qual eu trabalhei por um certo tempo. Pensei nos produtos que eram oferecidos e os preços. Com isso, pude formular um quadro de produtos e valores e criar, juntamente com o CLAUDE, um modelo de python que conseguisse automatizar os calculos de meta, quantidade vendida, despesas... Desta forma, consegui, da melhor maneira possivel, juntar os meus conhecimentos com as facilidades que  as inteligências artificiais oferecem para criar esse modelo que pode facilitar bastante o dia a dia de uma organização. Achei um trabalho muito interesssante e que me ensinou de forma muito pratica como se pode utilizar a linguagem em python dentro de uma empresa e evoluir um pouco mais na pratica dessa linguagem, utilizando um pouco de cada coisa que aprendemos ao longo do semestre e até coisas novas para mim que acabei aprendendo com as inteligências artificiais para aprimorar ainda mais o trabalho.