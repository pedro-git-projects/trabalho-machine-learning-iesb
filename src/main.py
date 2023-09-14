from processors.csv_processor import (
    calcular_somatorio_genero,
    plot_porcentagem_sobreviventes,
    processar_csv,
    scatter_age_vs_fare,
)
import os


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    processar_csv("../data/dados.csv", "../respostas/Resposta01.txt")
    calcular_somatorio_genero("../data/dados.csv")
    plot_porcentagem_sobreviventes(
        "../data/dados.csv", "../respostas/sobrevivtentes.png"
    )
    scatter_age_vs_fare("../data/dados.csv", "../respostas/scatter.png")


if __name__ == "__main__":
    main()
