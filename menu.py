from calculos import simular_periodo, calcular_meta
from arquivo import salvar_csv
#funcao p menu
def menu():
    historico = []
    while True:
        print("\n=== SIMULADOR DE INVESTIMENTOS PRO ===")
        print("1 - Simular por Tempo Fixo")
        print("2 - Calcular Tempo para Meta")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            dados = simular_periodo()
            historico.extend(dados)

        elif opcao == "2":
            dados = calcular_meta()
            historico.extend(dados)

        elif opcao == "0":
            if historico:
                nome = input("Digite o nome do arquivo CSV: ")
                salvar_csv(nome, historico)
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida.")