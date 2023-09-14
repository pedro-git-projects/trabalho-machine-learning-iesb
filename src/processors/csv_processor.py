import pandas as pd
import statistics
import matplotlib.pyplot as plt


"""
    Processa um arquivo CSV de entrada, tratando valores inválidos nas colunas 'age', calculando a moda das idades
    válidas e substituindo os valores inválidos pela moda. O resultado é salvo em um novo arquivo CSV.

    Args:
        input_file (str): O caminho do arquivo CSV de entrada.
        output_file (str): O caminho onde o arquivo processado será salvo.

    Raises:
        FileNotFoundError: Se o arquivo de entrada não for encontrado.
        pd.errors.ParserError: Se o arquivo de entrada não estiver em formato CSV válido.

    Example:
        Para processar um arquivo chamado 'dados.csv' e salvar o resultado em 'dados_processados.csv':
        >>> processar_csv('dados.csv', 'dados_processados.csv')
    """


def processar_csv(input_file: str, output_file: str) -> None:
    try:
        # lê o arquivo
        df = pd.read_csv(input_file)

        # remove valores inválidos
        valid_ages = df["age"].dropna()

        # calcula a moda das idades
        mode_ages = statistics.mode(valid_ages)

        # substitui as idades inválidas pela moda
        df["age"].fillna(mode_ages, inplace=True)

        # salva em um arquivo
        df.to_csv(output_file, index=False)

    except FileNotFoundError:
        print(f"O arquivo {input_file} não foi encontrado.")
    except pd.errors.ParserError:
        print(f"O arquivo {input_file} não está em formato CSV válido.")


def plot_porcentagem_sobreviventes(csv_file: str, output_file: str) -> None:
    try:
        df = pd.read_csv(csv_file)

        # contagem de sobreviventes e não sobreviventes
        sobreviventes = df["survived"].value_counts()

        # plotar o gráfico de pizza
        plt.figure(figsize=(6, 6))
        plt.pie(
            sobreviventes,
            labels=["Não Sobreviventes", "Sobreviventes"],
            autopct="%1.1f%%",
            startangle=140,
        )
        plt.title("Porcentagem de Sobreviventes e Não Sobreviventes")
        plt.savefig(output_file)

    except FileNotFoundError:
        print(f"O arquivo {csv_file} não foi encontrado.")
    except pd.errors.ParserError:
        print(f"O arquivo {csv_file} não está em formato CSV válido.")


def scatter_age_vs_fare(csv_file: str, save_path=None) -> None:
    try:
        df = pd.read_csv(csv_file)

        # criar um gráfico de dispersão de idade x tarifa
        plt.figure(figsize=(8, 6))
        plt.scatter(df["age"], df["fare"], alpha=0.5)
        plt.xlabel("Idade")
        plt.ylabel("Tarifa")
        plt.title("Dispersão de Idade X Tarifa")

        if save_path:
            # salva o gráfico de dispersão
            plt.savefig(save_path)
        else:
            # mostra o gráfico se nenhum caminho for especificado
            plt.show()

    except FileNotFoundError:
        print(f"O arquivo {csv_file} não foi encontrado.")
    except pd.errors.ParserError:
        print(f"O arquivo {csv_file} não está em formato CSV válido.")


def calcular_somatorio_genero(csv_file: str) -> None:
    try:
        df = pd.read_csv(csv_file)

        # calcula o somatório de homens e mulheres
        somatorio_genero = df["sex"].value_counts()

        # apresenta o somatório no terminal
        print("Somatório de Homens e Mulheres:")
        print(somatorio_genero)

    except FileNotFoundError:
        print(f"O arquivo {csv_file} não foi encontrado.")
    except pd.errors.ParserError:
        print(f"O arquivo {csv_file} não está em formato CSV válido.")
