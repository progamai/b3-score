# 📈 B3 Score

## 🇧🇷 Análise Fundamentalista de Empresas da B3

O **B3 Score** é uma aplicação interativa desenvolvida em **Python e Streamlit** para análise e comparação de empresas listadas na B3.

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

O B3 Score utiliza uma metodologia própria baseada em quatro indicadores fundamentalistas, com pontuação máxima de **100 pontos**.

| Indicador | Critério | Pontuação |
|---|---|---:|
| **P/L** | Entre 5 e 15 | +20 |
| **P/VP** | ≤ 1,5 | +20 |
| **ROE** | ≥ 20% | +30 |
| **ROE** | ≥ 15% | +22 |
| **ROE** | ≥ 10% | +15 |
| **Dividend Yield** | ≥ 8% | +30 |
| **Dividend Yield** | ≥ 6% | +22 |
| **Dividend Yield** | ≥ 4% | +15 |

> Para ROE e Dividend Yield, apenas a maior faixa atingida é considerada. As pontuações das faixas não são cumulativas.

### Classificação

| Score | Classificação |
|---:|---|
| **80–100** | 🟢 Excelente |
| **60–79** | 🔵 Boa |
| **40–59** | 🟡 Regular |
| **0–39** | 🔴 Ruim |

### Exemplo de cálculo

Considerando uma empresa com:

- P/L = 4,1 → **0 pontos**
- P/VP = 1,14 → **20 pontos**
- ROE = 27,7% → **30 pontos**
- Dividend Yield = 7% → **22 pontos**

O resultado será:

**B3 Score = 72/100**

A metodologia foi desenvolvida para fins educacionais e de demonstração de conhecimentos em coleta, tratamento, análise e visualização de dados.

---

# 🔍 Funcionalidades

## 📊 Análise individual

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

## ⚖️ Comparação entre empresas

A aplicação permite informar dois tickers e comparar:

- Score;
- P/L;
- P/VP;
- ROE;
- Dividend Yield.

Também são apresentados:

- 📊 Tabela comparativa;
- 📈 Gráfico comparativo;
- 🧠 Análise dos indicadores;
- 🏆 Empresa com maior Score;
- ✅ Pontos favoráveis de cada empresa.

### Exemplo

```text
Empresa 1: PETR4
Empresa 2: VALE3

PETR4 → 72/100
VALE3 → 22/100

PETR4 apresenta o maior B3 Score: 72 pontos.

---

# 🏆 Ranking por setor

A aplicação identifica o setor relacionado à empresa pesquisada e apresenta um ranking com empresas do mesmo segmento.

O ranking apresenta:

- Ticker;
- B3 Score;
- Classificação;
- Posição da empresa pesquisada;
- Gráfico comparativo do Score.

### Exemplo ilustrativo

```text
Ranking - Setor

Ticker    Score    Classificação
PETR4       72     🔵 Boa
PRIO3       45     🟡 Regular
BRAV3       25     🔴 Ruim

---

# 🧠 Insights automáticos

O módulo de comparação gera informações automáticas sobre os indicadores das empresas analisadas.

Entre os insights apresentados estão:

- 🏆 Empresa com maior B3 Score;
- ✅ Indicadores favoráveis de cada empresa;
- 📊 Comparação de P/L;
- 📊 Comparação de P/VP;
- 📈 Comparação de ROE;
- 💰 Comparação de Dividend Yield.

---

# 📥 Processo de dados

O projeto realiza a coleta de informações fundamentalistas utilizando requisições HTTP e técnicas de web scraping.

O processo é dividido em etapas:

```text
Coleta dos dados
       ↓
Tratamento dos dados
       ↓
Conversão dos indicadores
       ↓
Cálculo do B3 Score
       ↓
Classificação
       ↓
Ranking
       ↓
Visualização
       ↓
Insights

---

# 🏗️ Arquitetura do projeto

O projeto foi organizado de forma modular, separando as principais responsabilidades da aplicação.

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
- 📓 Jupyter Notebook
- 🔧 Git
- 🐙 GitHub

---

# ⚙️ Como executar o projeto

## 1. Clonar o repositório

```bash
git clone https://github.com/progamai/b3-score.git

# ⚙️ Como executar o projeto

## 2. Entrar na pasta

```bash
cd b3-score

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

---

# 📊 Fluxo da aplicação

```text
Usuário informa o ticker
          ↓
     Coleta dos dados
          ↓
   Tratamento dos dados
          ↓
   Cálculo dos indicadores
          ↓
      B3 Score
          ↓
      Classificação
          ↓
 ┌────────┴─────────┐
 ↓                  ↓
Ranking          Comparação
 ↓                  ↓
Setor             Insights
          ↓
     Visualização

     ---

# 🧪 Testes

O projeto possui uma estrutura de testes localizada em:

```text
tests/teste.py

---

# 📸 Demonstração

A aplicação possui uma interface interativa desenvolvida em Streamlit para análise individual, comparação de empresas e visualização de rankings.

### 🔎 Análise individual

A aplicação permite informar um ticker e visualizar:

- Empresa;
- Cotação;
- B3 Score;
- Classificação;
- Indicadores fundamentalistas;
- Composição do Score;
- Ranking dentro do setor.

### ⚖️ Comparação entre empresas

A aplicação permite comparar duas empresas, apresentando:

- B3 Score;
- P/L;
- P/VP;
- ROE;
- Dividend Yield;
- Gráfico comparativo;
- Insights automáticos.

### 🏆 Ranking por setor

A aplicação apresenta a posição da empresa pesquisada em relação às demais empresas do mesmo setor.

> 📌 Screenshots da aplicação serão adicionados nesta seção.

---

# ⚠️ Limitações

O B3 Score foi desenvolvido para fins educacionais e demonstração de conhecimentos em análise de dados.

Os resultados dependem da disponibilidade e qualidade dos dados coletados.

A metodologia utilizada representa uma regra de pontuação criada especificamente para este projeto e não constitui uma avaliação completa do valor ou da qualidade de uma empresa.

O projeto não considera, entre outros fatores:

- análise macroeconômica;
- análise técnica;
- projeções futuras;
- fluxo de caixa descontado;
- riscos específicos de cada empresa;
- cenário econômico futuro;
- perfil individual do investidor.

---

# ⚠️ Disclaimer

O **B3 Score não constitui recomendação de compra, venda ou manutenção de ativos financeiros**.

A aplicação possui finalidade exclusivamente educacional e demonstra técnicas de:

- coleta de dados;
- tratamento de dados;
- análise de indicadores;
- criação de métricas;
- visualização de dados;
- desenvolvimento de aplicações.

---

# 🚀 Próximas melhorias

Possíveis evoluções futuras do projeto:

- 📅 Histórico dos indicadores;
- 📈 Evolução histórica do Score;
- 📊 Inclusão de novos indicadores fundamentalistas;
- 🏦 Filtros avançados por setor;
- 🔎 Pesquisa avançada de empresas;
- 📥 Exportação dos resultados;
- 📊 Comparação de múltiplas empresas;
- ☁️ Deploy da aplicação;
- 🔄 Atualização automática dos dados.

---

# 👨‍💻 Autor

## Maicon Santos

Projeto desenvolvido como parte do meu portfólio de **Análise de Dados**, aplicando conhecimentos de Python, análise fundamentalista, tratamento de dados, visualização e desenvolvimento de dashboards.

### Principais conhecimentos aplicados

- Python;
- Pandas;
- SQL;
- Análise de Dados;
- Estatística;
- Visualização de Dados;
- Web Scraping;
- Streamlit;
- Git;
- GitHub.

### 🔗 Links

- GitHub: https://github.com/progamai
- Repositório do projeto: https://github.com/progamai/b3-score

---

# 📌 Status do projeto

🟢 **Projeto funcional**

O B3 Score possui:

- ✅ Coleta de dados;
- ✅ Tratamento dos dados;
- ✅ Cálculo do Score;
- ✅ Classificação;
- ✅ Ranking por setor;
- ✅ Comparação entre empresas;
- ✅ Gráficos interativos;
- ✅ Insights automáticos;
- ✅ Tratamento de tickers inválidos;
- ✅ Interface Streamlit;
- ✅ Testes;
- ✅ Versionamento com Git;
- ✅ Repositório público no GitHub.

---

⭐ Se este projeto foi útil ou interessante, considere deixar uma estrela no repositório.




