import xml.etree.ElementTree as ET

def analisar_faturamento_xml(caminho_arquivo):
    """
    Calcula e retorna informações sobre o faturamento mensal a partir de um arquivo XML.
    (Assumindo a estrutura XML fornecida: <row><dia>...</dia><valor>...</valor></row>)
    """
    try:
        tree = ET.parse(caminho_arquivo)
        root = tree.getroot()
    except FileNotFoundError:
        return "Erro: Arquivo XML não encontrado."
    except ET.ParseError:
        return "Erro: Arquivo XML inválido."

    faturamento_valido = []
    faturamento_todos = []

    for row in root.findall('row'):
        dia_element = row.find('dia')
        valor_element = row.find('valor')

        if valor_element is not None and valor_element.text:
            try:
                valor = float(valor_element.text)
                faturamento_todos.append(valor)
                if valor > 0:
                    faturamento_valido.append(valor)
            except ValueError:
                if dia_element is not None and dia_element.text:
                    print(f"Aviso: Valor de faturamento inválido encontrado para o dia {dia_element.text}.")
                else:
                    print("Aviso: Valor de faturamento inválido encontrado.")

    if not faturamento_valido:
        return {
            "menor_faturamento": 0,
            "maior_faturamento": max(faturamento_todos) if faturamento_todos else 0,
            "dias_acima_media": 0,
        }

    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_todos)
    media_mensal = sum(faturamento_valido) / len(faturamento_valido)
    dias_acima_media = sum(1 for row in root.findall('row')
                             if row.find('valor') is not None and float(row.find('valor').text) > media_mensal)

    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_media": dias_acima_media,
    }

if __name__ == "__main__":
    arquivo_xml = 'faturamento.xml'  # Certifique-se de que o nome do arquivo esteja correto
    resultados = analisar_faturamento_xml(arquivo_xml)

    if isinstance(resultados, str):
        print(resultados)
    else:
        print("Análise de Faturamento Mensal (XML):")
        print(f"Menor faturamento em um dia (desconsiderando dias sem faturamento): R$ {resultados['menor_faturamento']:.4f}")
        print(f"Maior faturamento em um dia: R$ {resultados['maior_faturamento']:.4f}")
        print(f"Número de dias com faturamento acima da média mensal: {resultados['dias_acima_media']}")