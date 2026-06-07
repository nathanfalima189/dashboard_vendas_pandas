# Importa a biblioteca Pandas para trabalhar com tabelas
import pandas as pd

# Importa o Matplotlib para criação de gráficos
import matplotlib.pyplot as plt

# Lê o arquivo CSV e transforma os dados em uma tabela
dados = pd.read_csv("vendas.csv")

# Cria uma nova coluna chamada Faturamento
dados["Faturamento"] = (
    dados["Quantidade"]
    * dados["Valor_Unitario"]
)

# Exibe título
print("=" * 50)
print("DASHBOARD DE VENDAS")
print("=" * 50)

# Calcula faturamento total
faturamento_total = dados["Faturamento"].sum()

print(f"\nFaturamento Total: R$ {faturamento_total:,.2f}")

# Agrupa produtos
produtos = dados.groupby("Produto")["Quantidade"].sum()

# Produto mais vendido
produto_mais_vendido = produtos.idxmax()

print(f"\nProduto Mais Vendido: {produto_mais_vendido}")

# Canal mais lucrativo
canal = dados.groupby("Canal_Venda")["Faturamento"].sum()

print(f"\nCanal Mais Lucrativo: {canal.idxmax()}")

# Forma de pagamento mais utilizada
pagamento = dados.groupby("Forma_Pagamento")["Pedido_ID"].count()

print(f"\nForma de Pagamento Mais Utilizada: {pagamento.idxmax()}")

# Estado com maior faturamento
estado = dados.groupby("Estado")["Faturamento"].sum()

print(f"\nEstado com Maior Faturamento: {estado.idxmax()}")

# Melhor vendedor
vendedor = dados.groupby("Vendedor")["Faturamento"].sum()

print(f"\nMelhor Vendedor: {vendedor.idxmax()}")

# Ticket médio
ticket_medio = (
    faturamento_total
    / dados["Pedido_ID"].nunique()
)

print(f"\nTicket Médio: R$ {ticket_medio:,.2f}")

# Cria gráfico
plt.figure(figsize=(10,6))

produtos.sort_values(
    ascending=False
).head(10).plot(
    kind="bar"
)

plt.title("Top 10 Produtos Mais Vendidos")
plt.xlabel("Produto")
plt.ylabel("Quantidade Vendida")

plt.tight_layout()

plt.savefig("grafico_produtos.png")

plt.show()

print("\nGráfico salvo como grafico_produtos.png")


# Agrupa faturamento por estado
faturamento_estado = dados.groupby(
    "Estado"
)["Faturamento"].sum()

# Cria gráfico
plt.figure(figsize=(8,5))

# Gera gráfico de barras
faturamento_estado.plot(
    kind="bar"
)

# Define título
plt.title(
    "Faturamento por Estado"
)

# Nome eixo X
plt.xlabel(
    "Estado"
)

# Nome eixo Y
plt.ylabel(
    "Faturamento (R$)"
)

# Ajusta layout
plt.tight_layout()

# Salva imagem
plt.savefig(
    "grafico_estados.png"
)

# Exibe gráfico
plt.show()

# Agrupa quantidade por forma de pagamento
pagamentos = dados.groupby(
    "Forma_Pagamento"
)["Pedido_ID"].count()

# Cria gráfico
plt.figure(figsize=(8,5))

# Gera gráfico
pagamentos.plot(
    kind="bar"
)

# Define título
plt.title(
    "Formas de Pagamento"
)

# Nome eixo X
plt.xlabel(
    "Forma de Pagamento"
)

# Nome eixo Y
plt.ylabel(
    "Quantidade de Pedidos"
)

# Ajusta layout
plt.tight_layout()

# Salva gráfico
plt.savefig(
    "grafico_pagamentos.png"
)

# Exibe gráfico
plt.show()