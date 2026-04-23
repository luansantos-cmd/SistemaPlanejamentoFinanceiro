import csv
import os
#função que vai salva o arquivo da "verificacao" de metas em csv separados a cada consulta
def salvar_csv(nome, dados):
    os.makedirs("resultados", exist_ok=True)
    caminho = f"resultados/{nome}.csv"

    with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["Mês", "Rendimento", "Saldo"])

        for linha in dados:
            writer.writerow(linha)
    print(f"Arquivo foi salvo em {caminho}")