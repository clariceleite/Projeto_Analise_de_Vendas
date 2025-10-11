# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot') 

dataframe = pd.read_csv("customer_journey.csv")
print(dataframe.head())
print("\n--- Tipos de Dados ---")
print(dataframe.info()) 
# %%
dataframe['Timestamp'] = pd.to_datetime(dataframe['Timestamp'])
print("\n--- Contagem de Valores Ausentes ---")
print(dataframe.isnull().sum())
# %%
# Porcentagem de sessões que resultaram em compra por país.
conversao_por_pais = dataframe.groupby('Country').agg(
    TotalSessoes=('SessionID', 'count'),
    TotalCompras=('Purchased', 'sum')
)
# %%
# Cálculo da Taxa de Conversão
conversao_por_pais['TaxaConversao'] = (
    conversao_por_pais['TotalCompras'] / conversao_por_pais['TotalSessoes']
) * 100
# %%
# Classificação e Visualização
conversao_por_pais = conversao_por_pais.sort_values(by='TaxaConversao', ascending=False)
print("\n--- Taxa de Conversão por País ---")
print(conversao_por_pais)
#%%
# Queremos saber onde os usuários passam mais tempo por tipo de dispositivo
engajamento_dispositivo = dataframe.groupby('DeviceType')['TimeOnPage_seconds'].mean().sort_values(ascending=False)
print("\n--- Tempo Médio na Página por Dispositivo ---")
print(engajamento_dispositivo)
# %%
# Taxa de Conversão por País (Barra)
plt.figure(figsize=(10, 6))
conversao_por_pais['TaxaConversao'].plot(kind='bar', color= sns.color_palette("viridis", len(conversao_por_pais)))
plt.title('Taxa de Conversão (%) por País')
plt.ylabel('Taxa de Conversão (%)')
plt.xlabel('País')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
# %%
# Engajamento por Dispositivo (Barra)
plt.figure(figsize=(8, 5))
engajamento_dispositivo.plot(kind='bar', color=['lightcoral', 'lightskyblue', 'lightgreen'])
plt.title('Tempo Médio de Engajamento por Dispositivo')
plt.ylabel('Tempo em Segundos (Média)')
plt.xlabel('Tipo de Dispositivo')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# %%
