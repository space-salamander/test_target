def inverter_string(texto):
    """
    Inverte os caracteres de uma string sem usar funções prontas como reverse().

    Args:
        texto (str): A string a ser invertida.

    Returns:
        str: A string com os caracteres em ordem inversa.
    """
    string_invertida = ""
    for i in range(len(texto) - 1, -1, -1):
        string_invertida += texto[i]
    return string_invertida

if __name__ == "__main__":
    # Opção 1: String previamente definida no código
    # minha_string = "Hello, World!"

    # Opção 2: String informada pelo usuário
    minha_string = input("Digite a string que você deseja inverter: ")

    string_invertida = inverter_string(minha_string)
    print(f"A string original é: {minha_string}")
    print(f"A string invertida é: {string_invertida}")