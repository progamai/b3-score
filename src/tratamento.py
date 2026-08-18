import pandas as pd


def converter_percentual(valor):

    if valor == "-":
        return None

    valor = valor.replace("%", "")
    valor = valor.replace(".", "")
    valor = valor.replace(",", ".")

    return float(valor)

def converter_numero(valor):

    if valor is None:
        return None

    valor = str(valor)

    if valor == "-" or valor == "None":
        return None

    valor = valor.replace(".", "")
    valor = valor.replace(",", ".")

    return float(valor)

def limpar_indicadores(df):

    df = df.copy()

    df.columns = ["Indicador", "Valor"]

    return df

def tratar_valores(df):

    df = df.copy()

    df["Valor"] = df["Valor"].astype(object)

    for i in df.index:

        valor = df.loc[i, "Valor"]
        
        if "%" in str(valor):
            df.loc[i, "Valor"] = converter_percentual(valor)
            
        else:
            df.loc[i, "Valor"] = converter_numero(valor)

    return df

def transformar_em_dicionario(df):

    return dict(zip(df["Indicador"], df["Valor"]))

def tratar_indicadores_bs4(indicadores):

    resultado = {}

    for chave, valor in indicadores.items():

        try:
            if "%" in str(valor):
                resultado[chave] = converter_percentual(valor)
            else:
                resultado[chave] = converter_numero(valor)

        except Exception:
            resultado[chave] = valor

    return resultado


