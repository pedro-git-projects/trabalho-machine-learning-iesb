import pandas as pd
import statistics


def processar_csv(input_file, output_file):
    try:
        df = pd.read_csv(input_file)

        valid_ages = df["age"].dropna()
        moda_idades = statistics.mode(valid_ages)

        df["age"].fillna(moda_idades, inplace=True)

        df.to_csv(output_file, index=False)

    except FileNotFoundError:
        print(f"O arquivo {input_file} não foi encontrado.")
    except pd.errors.ParserError:
        print(f"O arquivo {input_file} não está em formato CSV válido.")
