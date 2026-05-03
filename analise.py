import pandas as pd

# carregar dados
df = pd.read_csv(r"C:\Users\fabia\OneDrive\Documentos\vendas.csv")

# converter data
df['Data'] = pd.to_datetime(df['Data'])

# criar coluna de mês
df['Mes'] = df['Data'].dt.month

# total de vendas
total = df['Valor'].sum()
print("Faturamento total:", total)

# vendas por produto
print("\nVendas por produto:")
print(df.groupby('Produto')['Valor'].sum())

# vendas por região
print("\nVendas por região:")
print(df.groupby('Regiao')['Valor'].sum())

# salvar arquivo limpo
df.to_csv("vendas_tratado.csv", index=False)
