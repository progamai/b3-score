import streamlit as st
import pandas as pd

from src.ranking import (
    analisar_empresa,
    ranking_dataframe
)

from src.setores import descobrir_setor

from src.graficos import (
    grafico_score_setor,
    grafico_comparacao,
    grafico_gauge_score
)

from src.insights import gerar_insight_comparacao


st.set_page_config(
    page_title="B3 Score",
    page_icon="📈",
    layout="wide"
)


st.title("📈 B3 Score")


# =========================================================
# CAMPO PRINCIPAL
# =========================================================

ticker = st.text_input(
    "Digite o ticker da ação",
    value="PETR4"
)


# =========================================================
# COMPARAÇÃO ENTRE EMPRESAS
# =========================================================

st.subheader("📊 Comparar empresas")

col_comp1, col_comp2 = st.columns(2)


with col_comp1:

    ticker1 = st.text_input(
        "Empresa 1",
        value="PETR4"
    )


with col_comp2:

    ticker2 = st.text_input(
        "Empresa 2",
        value="VALE3"
    )


if st.button("Comparar"):

    ticker1_digitado = ticker1.strip().upper()
    ticker2_digitado = ticker2.strip().upper()

    if not ticker1_digitado or not ticker2_digitado:

        st.warning(
            "⚠️ Informe os dois tickers para realizar a comparação."
        )

        st.stop()

    try:

        empresa1 = analisar_empresa(
            ticker1_digitado
        )

        empresa2 = analisar_empresa(
            ticker2_digitado
        )

    except Exception:

        st.error(
            "❌ Não foi possível encontrar um dos tickers informados."
        )

        st.stop()

    # Verifica se os dados essenciais foram encontrados

    if (
        empresa1.get("Empresa") is None
        or empresa1.get("Cotação") is None
    ):

        st.error(
            f"❌ O ticker {ticker1_digitado} não foi encontrado "
            "ou não possui dados disponíveis."
        )

        st.stop()

    if (
        empresa2.get("Empresa") is None
        or empresa2.get("Cotação") is None
    ):

        st.error(
            f"❌ O ticker {ticker2_digitado} não foi encontrado "
            "ou não possui dados disponíveis."
        )

        st.stop()

    st.divider()

    st.subheader("📊 Comparação")

    col1, col2 = st.columns(2)

    # -----------------------------------------------------
    # EMPRESA 1
    # -----------------------------------------------------

    with col1:

        st.markdown(
            f"### {empresa1['Ticker']}"
        )

        st.metric(
            "Empresa",
            empresa1["Empresa"]
        )

        st.metric(
            "Score",
            f'{empresa1["Score"]}/100'
        )


    # -----------------------------------------------------
    # EMPRESA 2
    # -----------------------------------------------------

    with col2:

        st.markdown(
            f"### {empresa2['Ticker']}"
        )

        st.metric(
            "Empresa",
            empresa2["Empresa"]
        )

        st.metric(
            "Score",
            f'{empresa2["Score"]}/100'
        )


    # -----------------------------------------------------
    # TABELA DE INDICADORES
    # -----------------------------------------------------

    st.subheader("Indicadores")

    comparacao = {

        "Indicador": [
            "P/L",
            "P/VP",
            "ROE",
            "Dividend Yield",
            "Score"
        ],

        empresa1["Ticker"]: [
            empresa1["P/L"],
            empresa1["P/VP"],
            empresa1["ROE"],
            empresa1["Dividend Yield"],
            empresa1["Score"]
        ],

        empresa2["Ticker"]: [
            empresa2["P/L"],
            empresa2["P/VP"],
            empresa2["ROE"],
            empresa2["Dividend Yield"],
            empresa2["Score"]
        ]
    }


    df_comparacao = pd.DataFrame(
        comparacao
    )


    st.dataframe(
        df_comparacao,
        hide_index=True,
        width="stretch"
    )


    # -----------------------------------------------------
    # GRÁFICO COMPARATIVO
    # -----------------------------------------------------

    fig = grafico_comparacao(
        empresa1,
        empresa2
    )


    st.plotly_chart(
        fig,
        width="stretch"
    )


    # -----------------------------------------------------
    # INSIGHTS DA COMPARAÇÃO
    # -----------------------------------------------------

    insight = gerar_insight_comparacao(
        empresa1,
        empresa2
    )


    st.subheader(
        "🧠 Análise da comparação"
    )


    if insight["vencedora"]:

        st.success(
            f"🏆 {insight['vencedora']} apresenta o maior "
            f"B3 Score: {insight['score_vencedora']} pontos."
        )

    else:

        st.info(
            f"⚖️ As duas empresas possuem o mesmo B3 Score: "
            f"{insight['score_vencedora']} pontos."
        )


    col_insight1, col_insight2 = st.columns(2)


    # -----------------------------------------------------
    # INSIGHTS EMPRESA 1
    # -----------------------------------------------------

    with col_insight1:

        st.markdown(
            f"**{empresa1['Ticker']} — pontos favoráveis:**"
        )


        if insight["pontos_empresa1"]:

            for indicador in insight["pontos_empresa1"]:

                st.write(
                    f"✅ {indicador}"
                )

        else:

            st.write(
                "Nenhum indicador favorável exclusivo."
            )


    # -----------------------------------------------------
    # INSIGHTS EMPRESA 2
    # -----------------------------------------------------

    with col_insight2:

        st.markdown(
            f"**{empresa2['Ticker']} — pontos favoráveis:**"
        )


        if insight["pontos_empresa2"]:

            for indicador in insight["pontos_empresa2"]:

                st.write(
                    f"✅ {indicador}"
                )

        else:

            st.write(
                "Nenhum indicador favorável exclusivo."
            )


# =========================================================
# ANÁLISE INDIVIDUAL
# =========================================================

if st.button("Analisar"):

    ticker_digitado = ticker.strip().upper()

    if not ticker_digitado:

        st.warning(
            "⚠️ Digite um ticker para realizar a análise."
        )

        st.stop()

    try:

        empresa = analisar_empresa(
            ticker_digitado
        )

    except Exception:

        st.error(
            f"❌ Não foi possível analisar o ticker "
            f"{ticker_digitado}."
        )

        st.stop()

    nome_setor, empresas_setor = descobrir_setor(
        ticker_digitado
    )

    ranking = ranking_dataframe(
        empresas_setor
    )

    ranking = ranking.reset_index(
        drop=True
    )
    # -----------------------------------------------------
    # POSIÇÃO NO RANKING
    # -----------------------------------------------------

    posicao = ranking[
        ranking["Ticker"] == ticker.upper()
    ].index[0] + 1


    st.divider()


    col_esquerda, col_direita = st.columns(
        [2, 1]
    )


    # -----------------------------------------------------
    # INFORMAÇÕES DA EMPRESA
    # -----------------------------------------------------

    with col_esquerda:

        st.subheader(
            empresa["Empresa"]
        )


        st.metric(
            "Cotação",
            f'R$ {empresa["Cotação"]}'
        )


        st.metric(
            "Score",
            f'{empresa["Score"]}/100'
        )


        st.progress(
            empresa["Score"] / 100
        )

        st.subheader("🎯 B3 Score")

        gauge = grafico_gauge_score(
          empresa["Score"]
        )

        st.plotly_chart(
          gauge,
          width="stretch"
        )

        st.success(
            empresa["Classificação"]
        )


        # -------------------------------------------------
        # MEDALHA DO RANKING
        # -------------------------------------------------

        medalhas = {
            1: "🥇",
            2: "🥈",
            3: "🥉"
        }


        icone = medalhas.get(
            posicao,
            "🏅"
        )


        st.info(
            f"{icone} {ticker.upper()} ocupa a "
            f"{posicao}ª posição no setor "
            f"{nome_setor}."
        )


        # -------------------------------------------------
        # INDICADORES
        # -------------------------------------------------

        st.subheader(
            "Indicadores principais"
        )


        c1, c2 = st.columns(2)


        with c1:

            st.metric(
                "P/L",
                empresa["P/L"]
            )


            st.metric(
                "P/VP",
                empresa["P/VP"]
            )


        with c2:

            st.metric(
                "ROE",
                f'{empresa["ROE"]}%'
            )


            st.metric(
                "Dividend Yield",
                f'{empresa["Dividend Yield"]}%'
            )
        st.subheader("🧮 Composição do Score")

        pontos = empresa["Pontos"]

        st.write(
            f"**P/L:** +{pontos['P/L']} pontos"
        )

        st.write(
            f"**P/VP:** +{pontos['P/VP']} pontos"
        )

        st.write(
            f"**ROE:** +{pontos['ROE']} pontos"
        )

        st.write(
            f"**Dividend Yield:** +{pontos['Dividend Yield']} pontos"
        )
        st.divider()

        st.subheader("📚 Como o B3 Score é calculado?")

        with st.expander("Ver metodologia do Score"):

            st.markdown("""
            O **B3 Score** é uma metodologia própria desenvolvida neste projeto
            para comparar empresas utilizando indicadores fundamentalistas.

            A pontuação é calculada a partir de quatro indicadores:

            **P/L — Preço/Lucro**
    
            - Entre 5 e 15 → +15 pontos
            - Fora desse intervalo → +0 pontos

            **P/VP — Preço/Valor Patrimonial**
    
            - Menor ou igual a 1,5 → +15 pontos
            - Acima de 1,5 → +0 pontos

            **ROE — Retorno sobre o Patrimônio**
    
            - ROE ≥ 20% → +20 pontos
            - ROE ≥ 15% → +15 pontos
            - ROE ≥ 10% → +10 pontos
            - ROE < 10% → +0 pontos

            **Dividend Yield**
    
            - DY ≥ 8% → +20 pontos
            - DY ≥ 6% → +15 pontos
            - DY ≥ 4% → +10 pontos
            - DY < 4% → +0 pontos

            ### Classificação

            - 🟢 **Excelente:** Score ≥ 80
            - 🔵 **Boa:** Score entre 60 e 79
            - 🟡 **Regular:** Score entre 40 e 59
            - 🔴 **Ruim:** Score < 40

            > **Importante:** o B3 Score é um modelo próprio desenvolvido
            > para fins de análise e comparação neste projeto. Os critérios,
            > pesos e faixas de pontuação não representam uma recomendação
            > oficial de investimento da B3.
          """)
        st.divider()

        st.metric(
            "B3 Score",
            f'{empresa["Score"]}/100'
        )
        
    # -----------------------------------------------------
    # RANKING DO SETOR
    # -----------------------------------------------------

    with col_direita:

        st.subheader(
            f"🏆 Ranking - {nome_setor}"
        )


        st.dataframe(
            ranking[
                [
                    "Ticker",
                    "Score",
                    "Classificação"
                ]
            ],
            hide_index=True,
            width="stretch"
        )


        # -------------------------------------------------
        # GRÁFICO DO SETOR
        # -------------------------------------------------

        fig = grafico_score_setor(
            ranking,
            ticker
        )


        st.plotly_chart(
            fig,
            width="stretch"
        )