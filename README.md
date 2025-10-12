# 🚀 Projeto Básico de Análise de Dados: Jornada do Cliente e Conversão

## Visão Geral do Projeto

Este projeto é um exercício fundamental de **Análise Descritiva de Dados** utilizando **Python** e a biblioteca **Pandas**. O objetivo principal é analisar 
dados de sessões de usuários de um website de e-commerce para entender os padrões de comportamento, engajamento e conversão.

O foco da análise é responder a duas questões principais de negócio:

1.  Qual país apresenta a **maior taxa de conversão**?
2.  Qual tipo de dispositivo (**DeviceType**) demonstra o **maior engajamento**, tempo médio na página?

---
## 💾 Dados Utilizados

O projeto utiliza um dataset simulado de jornadas de clientes (fornecido como `customer_journey.csv`)

| Coluna | Descrição |
| :--- | :--- |
| `SessionID` | Identificador único de cada sessão de navegação. |
| `UserID` | Identificador único do usuário. |
| `Timestamp` | Data e hora da ação. |
| `PageType` | Tipo de página visitada (`home`, `product_page`, `cart`, etc.). |
| `DeviceType` | Tipo do dispositivo (`Desktop`, `Mobile`, `Tablet`). |
| `Country` | País de origem do usuário. |
| `ReferralSource` | Fonte de tráfego do usuário (Ex: Google, Email). |
| `TimeOnPage_seconds`| Tempo gasto pelo usuário na página em segundos. |
| `ItemsInCart` | Número de itens no carrinho após a ação. |
| `Purchased` | Indicador de compra (1 para compra, 0 para não compra). |

---
## 🛠️ Tecnologias e Bibliotecas

* **Linguagem:** Python
* **Manipulação de Dados:** Pandas
* **Visualização de Dados:** Matplotlib e Seaborn
* **Ambiente:** Jupyter Notebook

## 📊 Principais Análises Realizadas
###  Preparação e Limpeza de Dados

1.  Carregamento do arquivo CSV no Pandas DataFrame.
2.  Conversão da coluna `Timestamp` para o formato datetime para permitir análises temporais futuras (embora neste projeto a análise seja mais focada em categorias).
3.  Verificação inicial de valores ausentes (`NaN`).
   
### Análise de Conversão por País

A taxa de conversão é calculada como:

$$\text{Taxa de Conversão} = \frac{\sum \text{Compras}}{\sum \text{Sessões}} \times 100$$

O resultado é visualizado em um gráfico de barras para identificar os mercados de melhor desempenho, logo com maior conversão.

### Análise de Engajamento por Dispositivo

O engajamento é medido pelo tempo médio que os usuários passam em qualquer página do site (`TimeOnPage_seconds`).

$$\text{Engajamento Médio} = \frac{\sum \text{Tempo na Página}}{\sum \text{Sessões}}$$

O resultado é visualizado em um gráfico de pizza para identificar os dispositivos com o maior engajamento.
