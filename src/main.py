from processors.csv_processor import processar_csv 
import os


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    processar_csv("../data/dados.csv", "../respostas/Resposta01.txt")


if __name__ == "__main__":
    main()
