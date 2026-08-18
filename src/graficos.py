import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def grafico_score_setor(ranking, ticker):

    ranking_plot = ranking.copy()

    ranking_plot["Grupo"] = ranking_plot["Ticker"].apply(
        lambda x: (
            "Empresa pesquisada"
            if x == ticker.upper()
            else "Outras empresas"
        )
    )

    fig = px.bar(
        ranking_plot,
        x="Ticker",
        y="Score",
        color="Grupo",
        text="Score",
        color_discrete_map={
            "Empresa pesquisada": "#0d6efd",
            "Outras empresas": "#bdbdbd"
        }
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        showlegend=False,
        xaxis_title="Ticker",
        yaxis_title="Score",
        height=400,
        template="plotly_dark"
    )

    return fig


def grafico_comparacao(empresa1, empresa2):

    dados = {
        "Indicador": [
            "Score",
            "P/L",
            "P/VP",
            "ROE",
            "Dividend Yield"
        ],

        empresa1["Ticker"]: [
            empresa1["Score"],
            empresa1["P/L"],
            empresa1["P/VP"],
            empresa1["ROE"],
            empresa1["Dividend Yield"]
        ],

        empresa2["Ticker"]: [
            empresa2["Score"],
            empresa2["P/L"],
            empresa2["P/VP"],
            empresa2["ROE"],
            empresa2["Dividend Yield"]
        ]
    }

    df = pd.DataFrame(dados)

    df = df.melt(
        id_vars="Indicador",
        var_name="Empresa",
        value_name="Valor"
    )

    fig = px.bar(
        df,
        x="Indicador",
        y="Valor",
        color="Empresa",
        barmode="group",
        text="Valor"
    )

    fig.update_layout(
        template="plotly_dark",
        height=450,
        xaxis_title="Indicador",
        yaxis_title="Valor"
    )

    fig.update_traces(
        textposition="outside"
    )

    return fig


def grafico_gauge_score(score):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            title={
                "text": "B3 Score"
            },
            gauge={
                "axis": {
                    "range": [0, 100]
                },
                "bar": {
                    "color": "#0d6efd"
                },
                "steps": [
                    {
                        "range": [0, 39],
                        "color": "#dc3545"
                    },
                    {
                        "range": [40, 59],
                        "color": "#ffc107"
                    },
                    {
                        "range": [60, 79],
                        "color": "#0d6efd"
                    },
                    {
                        "range": [80, 100],
                        "color": "#198754"
                    }
                ],
                "threshold": {
                    "line": {
                        "color": "white",
                        "width": 4
                    },
                    "thickness": 0.75,
                    "value": score
                }
            }
        )
    )

    fig.update_layout(
        height=350,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        ),
        template="plotly_dark"
    )

    return fig

    fig.update_layout(
        height=350,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )
    )

    return fig