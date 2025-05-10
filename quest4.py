def calcular_percentual_faturamento(faturamento_por_estado):
    """
    Calcula o percentual de representação de cada estado no faturamento total.

    Args:
        faturamento_por_estado (dict): Um dicionário onde as chaves são os estados
                                       e os valores são o faturamento correspondente.

    Returns:
        dict: Um dicionário com os estados como chaves e seus percentuais
              de representação no faturamento total como valores.
    """
    total_faturamento = sum(faturamento_por_estado.values())
    percentuais = {}
    for estado, faturamento in faturamento_por_estado.items():
        percentual = (faturamento / total_faturamento) * 100
        percentuais[estado] = percentual
    return percentuais

if __name__ == "__main__":
    faturamento = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53,
    }

    percentuais_faturamento = calcular_percentual_faturamento(faturamento)

    print("Percentual de Representação do Faturamento por Estado:")
    for estado, percentual in percentuais_faturamento.items():
        print(f"{estado}: {percentual:.2f}%")