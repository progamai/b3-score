"""
Módulo: coleta.py

Responsável pela coleta de dados do projeto B3 Score.

Fontes:
- Yahoo Finance
- Fundamentus
"""
import pandas as pd
import requests

from bs4 import BeautifulSoup
from io import StringIO

def obter_html(ticker):
    url = f"https://www.fundamentus.com.br/detalhes.php?papel={ticker}"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/138.0.0.0 Safari/537.36"
        )
    }

    resposta = requests.get(url, headers=headers)

    resposta.raise_for_status()

    return resposta.text

def obter_tabelas(html):
    tabelas = pd.read_html(StringIO(html))
    return tabelas

def obter_indicadores(tabelas):

    indicadores = tabelas[2][[4, 5]].copy()

    indicadores.columns = ["Indicador", "Valor"]

    indicadores = indicadores.iloc[1:]

    indicadores["Indicador"] = (
        indicadores["Indicador"]
        .astype(str)
        .str.replace("?", "", regex=False)
        .str.strip()
    )

    indicadores["Valor"] = (
        indicadores["Valor"]
        .astype(str)
        .str.replace("?", "", regex=False)
        .str.strip()
    )

    indicadores.reset_index(drop=True, inplace=True)

    return indicadores

def obter_indicadores_bs4(html):

    soup = BeautifulSoup(html, "html.parser")

    dados = soup.find_all("td")

    indicadores = {}

    for i in range(len(dados) - 1):

        chave = dados[i].get_text(strip=True)

        valor = dados[i + 1].get_text(strip=True)

        if chave.startswith("?"):

            chave = chave.replace("?", "").strip()

            indicadores[chave] = valor

    return indicadores


