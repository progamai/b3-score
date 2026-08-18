def gerar_insight_comparacao(empresa1, empresa2):

    ticker1 = empresa1["Ticker"]
    ticker2 = empresa2["Ticker"]

    score1 = empresa1["Score"]
    score2 = empresa2["Score"]

    pontos_empresa1 = []
    pontos_empresa2 = []

    # =========================
    # P/L
    # =========================

    pl1 = empresa1.get("P/L")
    pl2 = empresa2.get("P/L")

    if pl1 is not None and 5 <= pl1 <= 15:
        pontos_empresa1.append(
            f"P/L ({pl1})"
        )

    if pl2 is not None and 5 <= pl2 <= 15:
        pontos_empresa2.append(
            f"P/L ({pl2})"
        )

    # =========================
    # P/VP
    # =========================

    pvp1 = empresa1.get("P/VP")
    pvp2 = empresa2.get("P/VP")

    if pvp1 is not None and pvp2 is not None:

        if pvp1 <= 1.5 and pvp2 > 1.5:
            pontos_empresa1.append("P/VP")

        elif pvp2 <= 1.5 and pvp1 > 1.5:
            pontos_empresa2.append("P/VP")

        elif pvp1 <= 1.5 and pvp2 <= 1.5:
            pontos_empresa1.append(
                f"P/VP ({pvp1})"
            )

            pontos_empresa2.append(
                f"P/VP ({pvp2})"
            )

    elif pvp1 is not None and pvp1 <= 1.5:

        pontos_empresa1.append(
            f"P/VP ({pvp1})"
        )

    elif pvp2 is not None and pvp2 <= 1.5:

        pontos_empresa2.append(
            f"P/VP ({pvp2})"
        )

    # =========================
    # ROE
    # =========================

    roe1 = empresa1.get("ROE")
    roe2 = empresa2.get("ROE")

    if roe1 is not None and roe2 is not None:

        if roe1 > roe2:
            pontos_empresa1.append("ROE")

        elif roe2 > roe1:
            pontos_empresa2.append("ROE")

    elif roe1 is not None:

        pontos_empresa1.append(
            f"ROE ({roe1}%)"
        )

    elif roe2 is not None:

        pontos_empresa2.append(
            f"ROE ({roe2}%)"
        )

    # =========================
    # Dividend Yield
    # =========================

    dy1 = empresa1.get("Dividend Yield")
    dy2 = empresa2.get("Dividend Yield")

    if dy1 is not None and dy2 is not None:

        if dy1 > dy2:
            pontos_empresa1.append("Dividend Yield")

        elif dy2 > dy1:
            pontos_empresa2.append("Dividend Yield")

    elif dy1 is not None:

        pontos_empresa1.append(
            f"Dividend Yield ({dy1}%)"
        )

    elif dy2 is not None:

        pontos_empresa2.append(
            f"Dividend Yield ({dy2}%)"
        )

    # =========================
    # Vencedora pelo Score
    # =========================

    if score1 > score2:

        vencedora = ticker1
        score_vencedora = score1
        score_perdedora = score2

    elif score2 > score1:

        vencedora = ticker2
        score_vencedora = score2
        score_perdedora = score1

    else:

        vencedora = None
        score_vencedora = score1
        score_perdedora = score2

    return {
        "vencedora": vencedora,
        "score_vencedora": score_vencedora,
        "score_perdedora": score_perdedora,
        "pontos_empresa1": pontos_empresa1,
        "pontos_empresa2": pontos_empresa2,
    }