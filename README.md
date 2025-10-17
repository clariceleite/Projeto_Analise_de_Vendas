# 🚀 Projeto Básico de Análise de Dados: Jornada do Cliente e Conversão

## Visão Geral do Projeto

Este projeto é um exercício fundamental de **Análise Descritiva de Dados** utilizando **Python** e a biblioteca **Pandas**. O objetivo principal é analisar 
dados de sessões de usuários de um website de e-commerce para entender os padrões de comportamento, engajamento e conversão.

O foco da análise é responder a duas questões principais de negócio:

1.  Qual país apresenta a **maior taxa de conversão**?
2.  Qual tipo de dispositivo (**DeviceType**) demonstra o **maior engajamento**, tempo médio na página?
3.  Qual é a diferença na **média de itens no carrinho** entre quem compra e quem não compra?
4.  Quais são as **melhores combinações de País e Dispositivo** em termos de taxa de conversão?

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

A taxa de conversão é calculada com o número de compras dividido pelo **número total de sessões únicas** (usando `SessionID` e o método `nunique`), multiplicado por 100.:

$$\text{Taxa de Conversão} = \frac{\sum \text{Compras}}{\sum \text{Sessões}} \times 100$$

O resultado é visualizado em um gráfico de Barras para identificar os mercados de melhor desempenho, logo com maior conversão.

### Análise de Engajamento por Dispositivo

O engajamento é medido pelo tempo médio que os usuários passam em qualquer página do site (`TimeOnPage_seconds`).

$$\text{Engajamento Médio} = \frac{\sum \text{Tempo na Página}}{\sum \text{Sessões}}$$

O resultado é visualizado em um gráfico de Pizza para identificar a distribuição do engajamento entre os dispositivos.

### Análise de Itens no Carrinho (Compradores vs. Não-Compradores)

Esta análise tem como objetivo investigar o **comportamento de intenção de compra**. Compara-se a média de itens adicionados ao carrinho (`ItemsInCart`) 
entre as sessões que finalizaram a compra (`Purchased = 1`) e as que não finalizaram (`Purchased = 0`).

O resultado é visualizado em um gráfico de Barras para comparação direta das médias.

### Análise Combinada entre País e Dispositivo

Cria-se uma análise entrelaçada para identificar as combinações específicas de `Country` e `DeviceType` que geram as maiores taxas de conversão.

O resultado é visualizado em uma tabela com o **Top 10** das combinações e um gráfico de Barras para ilustrar essas combinações de melhor performance.

## 📈 Resultados da Análise
### Taxa de Conversão 
<img width="889" height="490" alt="image" src="https://github.com/user-attachments/assets/387b9f49-3bbf-4714-b730-c873b7498235" />

### Taxa de Engajamento
<img width="784" height="799" alt="image" src="https://github.com/user-attachments/assets/5e3b4612-6d13-4ecb-ac54-27b5b37f7134" />

#### Média de Itens no Carrinho
<img width="789" height="590" alt="image" src="https://github.com/user-attachments/assets/e424341a-71c5-40b0-aaa3-2e8c527d54d4" />

#### Top 10 Combinações País + Dispositivo
<img width="989" height="590" alt="image" src="https://github.com/user-attachments/assets/aa8b6e62-3e45-4fe2-8dce-efedad9f57da" />
