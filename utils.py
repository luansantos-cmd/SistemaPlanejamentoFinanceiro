#tratamento de excecoes
#try except
def ler_float(msg):
    while True:
        try:
            valor = float(input(msg))

            if valor < 0:
                print("Digite valor positivo.")
            else:
                return valor

        except:
            print("Entrada inválida.")


def ler_int(msg):
    while True:
        try:
            valor = int(input(msg))

            if valor <= 0:
                print("Digite número maior que zero.")
            else:
                return valor

        except:
            print("Entrada inválida.")