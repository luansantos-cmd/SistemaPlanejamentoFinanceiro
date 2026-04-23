from utils import ler_float, ler_int
#entradas
def simular_periodo():
    valor = ler_float("Valor inicial: ")
    aporte = ler_float("Aporte mensal: ")
    taxa = ler_float("Taxa de juros mensal (%): ")
    meses = ler_int("Quantidade de meses: ")
    dados = []
    
    print("\n--- Evolução do Investimento ---")
#aqui calculo da evolucao mensal de patrimonio
    for mes in range(1, meses + 1):
        rendimento = valor * (taxa / 100)
        valor += rendimento + aporte

        print(f"Mês {mes}: Rendimento = R$ {rendimento:.2f} -- Saldo = R$ {valor:.2f}")

        dados.append([mes, round(rendimento, 2), round(valor, 2)])

    return dados


def calcular_meta():
    valor = ler_float("Valor inicial: ")
    aporte = ler_float("Aporte mensal: ")
    taxa = ler_float("Taxa de juros mensal (%): ")
    meta = ler_float("Valor desejado: ")
    dados = []
    mes = 0

    print("\n--- Buscando meta financeira ---")
#ja aqui o calculo de quantos meses são necessários para atingir ou ultrapassar a meta.
    while valor < meta:
        mes += 1
        rendimento = valor * (taxa / 100)
        valor += rendimento + aporte

        print(f"Mês {mes}: Rendimento = R$ {rendimento:.2f} | Saldo = R$ {valor:.2f}")
        dados.append([mes, round(rendimento, 2), round(valor, 2)])

    print(f"\nMeta será atingida em {mes} meses!")

    return dados