# 📈 B3 Score

## 🇧🇷 Análise Fundamentalista de Empresas da B3

O **B3 Score** é uma aplicação interativa desenvolvida em Python e Streamlit para análise e comparação de empresas listadas na B3.

O projeto transforma indicadores fundamentalistas em uma pontuação de **0 a 100 pontos**, permitindo avaliar empresas individualmente, comparar diferentes ativos e visualizar o posicionamento de uma empresa em relação a outras do mesmo setor.

> ⚠️ **Aviso:** O B3 Score é uma ferramenta educacional e de análise de dados. Não constitui recomendação de compra ou venda de ativos financeiros.

---

## 🎯 Objetivo

O objetivo do projeto é transformar dados financeiros em informações mais simples e visualmente acessíveis para apoiar análises fundamentalistas.

A aplicação permite:

- 🔎 Pesquisar uma empresa pelo ticker;
- 📊 Consultar indicadores fundamentalistas;
- 🧮 Calcular um Score de 0 a 100;
- 🏆 Classificar a empresa de acordo com sua pontuação;
- 📈 Comparar duas empresas;
- 🏭 Identificar o setor da empresa;
- 🥇 Visualizar o ranking dentro do setor;
- 📊 Visualizar gráficos comparativos;
- 🧠 Gerar insights automáticos sobre os indicadores;
- 🎯 Visualizar a composição do B3 Score.

---

# 📊 Metodologia do B3 Score

O Score é calculado utilizando quatro indicadores fundamentalistas:

| Indicador | Critério | Pontuação |
|---|---|---:|
| **P/L** | Entre 5 e 15 | +15 |
| **P/VP** | ≤ 1,5 | +15 |
| **ROE** | ≥ 20% | +20 |
| **ROE** | ≥ 15% | +15 |
| **ROE** | ≥ 10% | +10 |
| **Dividend Yield** | ≥ 8% | +20 |
| **Dividend Yield** | ≥ 6% | +15 |
| **Dividend Yield** | ≥ 4% | +10 |

### Classificação

| Score | Classificação |
|---:|---|
| **80–100** | 🟢 Excelente |
| **60–79** | 🔵 Boa |
| **40–59** | 🟡 Regular |
| **0–39** | 🔴 Ruim |

A pontuação foi desenvolvida como uma metodologia própria para fins de análise e demonstração de conhecimentos em tratamento de dados, análise exploratória, criação de indicadores e desenvolvimento de aplicações.

---

# 🔍 Funcionalidades

## Análise individual

Ao informar um ticker, a aplicação apresenta:

- Empresa;
- Cotação;
- B3 Score;
- Classificação;
- P/L;
- P/VP;
- ROE;
- Dividend Yield;
- Composição da pontuação;
- Ranking da empresa dentro do setor.

---

## 📊 Comparação entre empresas

A aplicação permite informar dois tickers e comparar:

- Score;
- P/L;
- P/VP;
- ROE;
- Dividend Yield.

Também são apresentados:

- 📊 Gráfico comparativo;
- 🧠 Análise dos indicadores;
- 🏆 Empresa com maior Score;
- ✅ Pontos favoráveis de cada empresa.

---

## 🏆 Ranking por setor

A aplicação identifica o setor da empresa pesquisada e apresenta um ranking com outras empresas do mesmo segmento.

Exemplo:

```text
🏆 Ranking - Petróleo

Ticker    Score    Classificação
REC...      60     🔵 Boa
PETR4       50     🟡 Regular
PRIO3       25     🔴 Ruim
BRAV3       15     🔴 

---

# 🛠️ Tecnologias utilizadas

- 🐍 Python
- 📊 Pandas
- 📈 Plotly
- 🎨 Streamlit
- 🌐 Requests
- 🔎 BeautifulSoup4
- 🔢 NumPy
- 🧪 Pytest
- 🗃️ Git e GitHub

---

# 🏗️ Estrutura do projeto

```text
b3-score/
│
├── app.py
│
├── src/
│   ├── coleta.py
│   ├── tratamento.py
│   ├── score.py
│   ├── ranking.py
│   ├── setores.py
│   ├── graficos.py
│   └── insights.py
│
├── notebooks/
│   ├── 01_coleta_dados.ipynb
│   └── 02_indicadores_fundamentalistas.ipynb
│
├── tests/
│   └── teste.py
│
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md