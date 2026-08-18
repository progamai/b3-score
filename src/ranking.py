import pandas as pd
from src.coleta import obter_html, obter_indicadores_bs4
from src.tratamento import tratar_indicadores_bs4
from src.score import calcular_score, classificar_score


def analisar_empresa(ticker):

    html = obter_html(ticker)

    indicadores = obter_indicadores_bs4(html)

    indicadores = tratar_indicadores_bs4(indicadores)

    score, detalhes, pontos = calcular_score(indicadores)

    classificacao = classificar_score(score)

    return {
        "Ticker": ticker,
        "Empresa": indicadores.get("Empresa"),
        "Cotação": indicadores.get("Cotação"),
        "P/L": indicadores.get("P/L"),
        "P/VP": indicadores.get("P/VP"),
        "ROE": indicadores.get("ROE"),
        "Dividend Yield": indicadores.get("Div. Yield"),
        "Score": score,
        "Classificação": classificacao,
        "Pontos": pontos,
    }

def analisar_setor(lista_empresas):

    ranking = []

    for ticker in lista_empresas:

        try:
            empresa = analisar_empresa(ticker)
            ranking.append(empresa)

        except Exception as e:
            print(f"Erro ao analisar {ticker}: {e}")

    ranking.sort(
        key=lambda empresa: empresa["Score"],
        reverse=True
    )

    return ranking

def ranking_dataframe(lista_empresas):

    ranking = analisar_setor(lista_empresas)

    df = pd.DataFrame(ranking)

    # Remove empresas sem dados
    df = df.dropna(subset=["Empresa"])

    return df