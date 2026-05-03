Análise de Vendas
 
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Carregar dados
df = pd.read_csv(r"C:\Users\fabia\OneDrive\Documentos\vendas.csv")

# Exemplo: animação por Data (precisa ser coluna categórica ou convertida)
df["Data"] = pd.to_datetime(df["Data"])
df["Data_str"] = df["Data"].dt.strftime("%Y-%m-%d")

# Gráfico animado
fig = px.bar(
    df,
    x="Produto",
    y="Valor",
    color="Categoria",
    animation_frame="Data_str",
    title="Vendas por Produto ao Longo do Tempo"
)

# Dashboard
app = Dash(__name__)
app.layout = html.Div([
    html.H1("Dashboard Animado de Vendas"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)

