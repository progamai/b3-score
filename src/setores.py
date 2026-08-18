BANCOS = [
    "BBAS3",
    "ITUB4",
    "BBDC4",
    "SANB11",
    "BPAC11",
]

PETROLEO = [
    "PETR4",
    "PRIO3",
    "RECV3",
    "BRAV3",
    "RRRP3",
]

MINERACAO = [
    "VALE3",
    "CSNA3",
    "USIM5",
    "GGBR4",
]

ENERGIA = [
    "EGIE3",
    "TAEE11",
    "CMIG4",
    "CPFE3",
]

SETORES = {
    "Bancos": BANCOS,
    "Petróleo": PETROLEO,
    "Mineração": MINERACAO,
    "Energia": ENERGIA,
}

def descobrir_setor(ticker):

    for nome, empresas in SETORES.items():

        if ticker in empresas:
            return nome, empresas

    return "Outros", [ticker]

