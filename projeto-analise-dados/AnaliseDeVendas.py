# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataframe = pd.read_csv("customer_journey.csv")
print(dataframe.head())
print("\n--- Tipos de Dados ---")
print(dataframe.info()) 
#%%
# Convertendo a coluna 'Timestamp' para o tipo datetime
dataframe['Timestamp'] = pd.to_datetime(dataframe['Timestamp'])
print("\n--- Contagem de Valores Ausentes ---")
print(dataframe.isnull().sum())
#%%
# Porcentagem de sessões que resultaram em compra por país.
conversao_pais = dataframe.groupby('Country').agg(
    total_sessoes=('SessionID', 'nunique'),
    total_compras=('Purchased', 'sum')
)

#%%
# Cálculo da Taxa de Conversão
conversao_pais['taxa_conversao'] = (conversao_pais['total_compras'] / conversao_pais['total_sessoes']) * 100
# Classificação e Visualização
conversao_pais = conversao_pais.sort_values(by='taxa_conversao', ascending=False)
print("\n--- Taxa de Conversão por País ---")
print(conversao_pais)

#%%
# Queremos saber onde os usuários passam mais tempo por tipo de dispositivo
engajamento_dispositivo = dataframe.groupby('DeviceType')['TimeOnPage_seconds'].mean().sort_values(ascending=False)
print("\n--- Tempo Médio na Página por Dispositivo ---")
print(engajamento_dispositivo)

# %%
# Taxa de Conversão por País (Barra)
x_paises = conversao_pais.index
y_taxas = conversao_pais['taxa_conversao']
cores = sns.color_palette("viridis", len(conversao_pais))
plt.figure(figsize=(9, 5))
plt.bar(x_paises, y_taxas, color=cores)
plt.title('Taxa de Conversão (%) por País')
plt.ylabel('Taxa de Conversão (%)')
plt.xlabel('País')
plt.tight_layout()
plt.show()

# %%
# Grafico Distribuição de Engajamento por Dispositivo
medias = engajamento_dispositivo.values
tipos_despositivo = engajamento_dispositivo.index
cores = sns.color_palette("viridis", len(conversao_pais))
plt.figure(figsize=(8, 8)) 
plt.pie(medias,labels=tipos_despositivo,autopct='%1.1f%%',startangle=90,colors=cores,
        wedgeprops={'edgecolor': 'black', 'linewidth': 1})

plt.title('Distribuição Percentual do Engajamento por Dispositivo')
plt.axis('equal')
plt.tight_layout()
plt.show()

# %%
# Análise de Itens no Carrinho
itens_carrinho = dataframe.groupby("Purchased")['ItemsInCart'].mean()
print("\n--- Média de Itens no Carrinho ---")
print(itens_carrinho)

# %%
# Gráfico Comparação de Itens no Carrinho
categorias = ['Não Comprou', 'Comprou']
medias_itens = [itens_carrinho[0], itens_carrinho[1]]
cores = sns.color_palette("viridis", len(conversao_pais))
plt.figure(figsize=(8, 6))
plt.bar(categorias, medias_itens, color=cores, edgecolor='black', linewidth=1.5)
plt.title('Média de Itens no Carrinho: Compradores vs Não-Compradores')
plt.ylabel('Média de Itens')
plt.xlabel('Status de Compra')
plt.tight_layout()
plt.show()

# %%
# Análise Combinada do País com o Dispositivo (Top Combinações)
combinacao = dataframe.groupby(['Country', 'DeviceType']).agg(
    total_sessoes=('SessionID', 'nunique'),
    total_compras=('Purchased', 'sum')
)
combinacao['taxa_conversao'] = (combinacao['total_compras'] / combinacao['total_sessoes']) * 100
combinacao = combinacao.sort_values(by='taxa_conversao', ascending=False).head(10)
print("\n--- Top 10 Combinações País + Dispositivo (Taxa de Conversão) ---")
print(combinacao)

# %%
# Gráfico de Barras para Combinações
combinacao.reset_index(inplace=True)
combinacoes = combinacao.apply(lambda row: f"{row['Country']} - {row['DeviceType']}", axis=1)
taxas = combinacao['taxa_conversao']
cores = sns.color_palette("viridis", len(combinacao))
plt.figure(figsize=(10, 6))
plt.bar(combinacoes, taxas, color=cores)
plt.title('Top 10 Combinações País + Dispositivo (Taxa de Conversão)')
plt.ylabel('Taxa de Conversão (%)')
plt.xlabel('Combinação País + Dispositivo')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
# %%

