def calcular_score(indicadores):

    score = 0
    detalhes = []
    pontos = {}

    # =========================
    # P/L
    # =========================

    pl = indicadores.get("P/L")

    if pl is not None and 5 <= pl <= 15:
        score += 20
        pontos["P/L"] = 20
        detalhes.append("✅ P/L entre 5 e 15 (+20)")
    else:
        pontos["P/L"] = 0
        detalhes.append("❌ P/L fora do intervalo (+0)")

    # =========================
    # P/VP
    # =========================

    pvp = indicadores.get("P/VP")

    if pvp is not None and pvp <= 1.5:
        score += 20
        pontos["P/VP"] = 20
        detalhes.append("✅ P/VP <= 1.5 (+20)")
    else:
        pontos["P/VP"] = 0
        detalhes.append("❌ P/VP > 1.5 (+0)")

    # =========================
    # ROE
    # =========================

    roe = indicadores.get("ROE")

    if roe is not None:

        if roe >= 20:
            score += 30
            pontos["ROE"] = 30
            detalhes.append("✅ ROE >= 20% (+30)")

        elif roe >= 15:
            score += 22
            pontos["ROE"] = 22
            detalhes.append("✅ ROE >= 15% (+22)")

        elif roe >= 10:
            score += 15
            pontos["ROE"] = 15
            detalhes.append("✅ ROE >= 10% (+15)")

        else:
            pontos["ROE"] = 0
            detalhes.append("❌ ROE abaixo de 10% (+0)")

    else:
        pontos["ROE"] = 0
        detalhes.append("❌ ROE não disponível (+0)")

    # =========================
    # Dividend Yield
    # =========================

    dy = indicadores.get("Div. Yield")

    if dy is not None:

        if dy >= 8:
            score += 30
            pontos["Dividend Yield"] = 30
            detalhes.append("✅ Dividend Yield >= 8% (+30)")

        elif dy >= 6:
            score += 22
            pontos["Dividend Yield"] = 22
            detalhes.append("✅ Dividend Yield >= 6% (+22)")

        elif dy >= 4:
            score += 15
            pontos["Dividend Yield"] = 15
            detalhes.append("✅ Dividend Yield >= 4% (+15)")

        else:
            pontos["Dividend Yield"] = 0
            detalhes.append("❌ Dividend Yield abaixo de 4% (+0)")

    else:
        pontos["Dividend Yield"] = 0
        detalhes.append("❌ Dividend Yield não disponível (+0)")

    return score, detalhes, pontos


def classificar_score(score):

    if score >= 80:
        return "🟢 Excelente"

    elif score >= 60:
        return "🔵 Boa"

    elif score >= 40:
        return "🟡 Regular"

    else:
        return "🔴 Ruim"