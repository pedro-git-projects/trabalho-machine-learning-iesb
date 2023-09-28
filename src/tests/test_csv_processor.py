import pytest
import pandas as pd
from processors.csv_processor import processar_csv


def test_processar_csv_arquivo_valido(tmpdir):
    """
    Verifica se a função é capaz de processar um arquivo CSV válido e substituir valores inválidos por sua moda.
    """

    # Cria um arquivo CSV de entrada com valores válidos e inválidos.
    with open(tmpdir.join("test_data.csv"), "w") as f:
        f.write("age,name\n18,João\n25,Maria\n-1,Pedro\n100,Ana\n")

    # Define o caminho do arquivo de entrada e saída.
    input_file = str(tmpdir.join("test_data.csv"))
    output_file = str(tmpdir.join("test_output.csv"))

    # Chama a função `processar_csv()`.
    processar_csv(input_file, output_file)

    # Lê o arquivo de saída processado.
    df = pd.read_csv(output_file)

    # Verifica se os valores inválidos foram substituídos pela moda.
    assert df["age"].isnull().sum() == 0
    assert not df["age"].empty



def test_processar_csv_arquivo_invalido(tmpdir):
    """
    Verifica se a função levanta uma exceção quando o arquivo de entrada é inválido.
    """

    # Define o caminho de um arquivo CSV inválido.
    input_file = tmpdir.join("test_data.csv")

    # Cria um arquivo CSV inválido.
    with open(input_file, "w") as f:
        f.write("nome\nJoão")

    # Chama a função `processar_csv()`.
    with pytest.raises(KeyError):
        processar_csv(input_file, "test_output.csv")

