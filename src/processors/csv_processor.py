import pandas as pd
import statistics
import matplotlib.pyplot as plt
from pandas.errors import ParserError


def processar_csv(input_file: str, output_file: str) -> str:
    """
    Processa um arquivo CSV de entrada, tratando valores inválidos nas colunas 'age', calculando a moda das idades
    válidas e substituindo os valores inválidos pela moda. O resultado é salvo em um novo arquivo CSV.

    Returns:
        str: Retona uma string com a mensagem de sucesso ou erro

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

    try:
        df = pd.read_csv(input_file)

        valid_ages = df["age"].dropna()
        mode_ages = statistics.mode(valid_ages)
        df["age"].fillna(mode_ages, inplace=True)

        df.to_csv(output_file, index=False)
        return f" Arquivo CSV processado com sucesso. Saída salva em {output_file}"

    except FileNotFoundError:
        return f"O arquivo {input_file} não foi encontrado."
    except pd.errors.ParserError:
        return f"O arquivo {input_file} não está em formato CSV válido."


def calcular_somatorio_genero(csv_file: str) -> str:
    """
    Calcula o somatório de homens e mulheres com base nos dados de um arquivo CSV
    e apresenta o resultado no terminal.

    Args:
        csv_file (str): O caminho para o arquivo CSV contendo os dados.

    Returns:
        str: Retona uma string com a mensagem de sucesso ou erro


    Raises:
        FileNotFoundError: Se o arquivo CSV especificado não for encontrado.
        pd.errors.ParserError: Se o arquivo CSV não estiver em formato válido.

    Example:
        calcular_somatorio_genero('dados.csv')
    """
    try:
        df = pd.read_csv(csv_file)

        somatorio_genero = df["sex"].value_counts()
        total_homens = somatorio_genero.get("male", 0)
        total_mulheres = somatorio_genero.get("female", 0)
        if total_mulheres is None or total_homens is None:
            raise ParserError

        total = total_homens + total_mulheres

        return f"Total de Homens: {total_homens}\n Total de Mulheres: {total_mulheres}\n Total Geral: {total}"

    except FileNotFoundError:
        return f"O arquivo {csv_file} não foi encontrado."
    except pd.errors.ParserError:
        return f"O arquivo {csv_file} não está em formato CSV válido."


def plot_porcentagem_sobreviventes(csv_file: str, output_file: str) -> str:
    """
    Gera um gráfico de pizza representando a porcentagem de sobreviventes e não sobreviventes
    com base nos dados de um arquivo CSV e salva o gráfico em um arquivo de saída.

    Args:
        csv_file (str): O caminho para o arquivo CSV contendo os dados.
        output_file (str): O caminho para o arquivo de saída onde o gráfico será salvo.

    Returns:
        str: Retona uma string com a mensagem de sucesso ou erro


    Raises:
        FileNotFoundError: Se o arquivo CSV especificado não for encontrado.
        pd.errors.ParserError: Se o arquivo CSV não estiver em formato válido.

    Example:
        plot_porcentagem_sobreviventes('dados.csv', 'grafico_pizza.png')
    """

    try:
        df = pd.read_csv(csv_file)

        sobreviventes = df["survived"].value_counts()

        plt.figure(figsize=(6, 6))
        plt.pie(
            sobreviventes,
            labels=["Não Sobreviventes", "Sobreviventes"],
            autopct="%1.1f%%",
            startangle=140,
        )
        plt.title("Porcentagem de Sobreviventes e Não Sobreviventes")
        plt.savefig(output_file)
        return f"Gráfico de porcentagem de sobreviventes e não sobreviventes plotado e salvo em {output_file}"

    except FileNotFoundError:
        return f"O arquivo {csv_file} não foi encontrado."
    except pd.errors.ParserError:
        return f"O arquivo {csv_file} não está em formato CSV válido."


def plota_dispersao_idade_tarifa(csv_file: str, save_path=None) -> str:
    """
    Cria um gráfico de dispersão para visualizar a relação entre a idade e a tarifa
    com base nos dados de um arquivo CSV. O gráfico pode ser salvo em um arquivo ou exibido na tela.

    Args:
        csv_file (str): O caminho para o arquivo CSV contendo os dados.
        save_path (str, optional): O caminho para salvar o gráfico. Se None, o gráfico será exibido na tela.
                                   (default is None)

    Returns:
        str: Retona uma string com a mensagem de sucesso ou erro


    Raises:
        FileNotFoundError: Se o arquivo CSV especificado não for encontrado.
        pd.errors.ParserError: Se o arquivo CSV não estiver em formato válido.

    Example:
        scatter_age_vs_fare('dados.csv', save_path='grafico_dispersao.png')
    """

    try:
        df = pd.read_csv(csv_file)

        plt.figure(figsize=(8, 6))
        plt.scatter(df["age"], df["fare"], alpha=0.5)
        plt.xlabel("Idade")
        plt.ylabel("Tarifa")
        plt.title("Dispersão de Idade X Tarifa")

        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()
        return f"Gráfico de dispersão plotado e salvo em {save_path}"

    except FileNotFoundError:
        return f"O arquivo {csv_file} não foi encontrado."
    except pd.errors.ParserError:
        return f"O arquivo {csv_file} não está em formato CSV válido."
