def gerar_fibonacci(n):
    """Gera os primeiros n números da sequência de Fibonacci."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        lista_fib = [0, 1]
        while len(lista_fib) < n:
            proximo_fib = lista_fib[-1] + lista_fib[-2]
            lista_fib.append(proximo_fib)
        return lista_fib

def verificar_fibonacci(numero, sequencia_fibonacci):
    """Verifica se um número está presente na sequência de Fibonacci."""
    if numero in sequencia_fibonacci:
        return True
    else:
        return False

if __name__ == "__main__":
    quantidade = int(input("Digite quantos números da sequência de Fibonacci você deseja gerar: "))
    sequencia = gerar_fibonacci(quantidade)
    print(f"Os primeiros {quantidade} números da sequência de Fibonacci são: {sequencia}")

    valor_para_verificar = int(input("Digite um valor para verificar se ele está na sequência: "))
    esta_na_sequencia = verificar_fibonacci(valor_para_verificar, sequencia)

    if esta_na_sequencia:
        print(f"O número {valor_para_verificar} está presente na sequência de Fibonacci gerada.")
    else:
        print(f"O número {valor_para_verificar} não está presente na sequência de Fibonacci gerada.")