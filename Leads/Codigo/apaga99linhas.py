import pandas as pd
from datetime import datetime


def apagarLinhas():
    # Carrega a pl  anilha
    caminho_arquivo_csv = r"C:\Users\user\Downloads\Leads\Para apagar - Copia.csv"  # Altere para o caminho da sua planilha
    encodings = ['utf-8', 'latin1', 'iso-8859-1']
    for encoding in encodings:
        try:
            df = pd.read_csv(caminho_arquivo_csv, encoding=encoding)
            break  # Se conseguiu ler com sucesso, interrompe o loop
        except UnicodeDecodeError:
            continue  # Se ocorrer um erro de decodificação, tenta o próximo encoding

    # Remove as primeiras 99 linhas, começando da segunda linha (índice 1)
    df = df.iloc[99:]
    HORA = datetime.now()
    quantidade_linhas = len(df)

    caminho_planilha_sem_primeiras_linhas = r"C:\Users\user\Downloads\Leads\Para apagar.csv" # Altere para o caminho onde deseja salvar a planilha
    df.to_csv(caminho_planilha_sem_primeiras_linhas, index=False)

    print(HORA)
    print(f"As primeiras 99 linhas foram removidas da planilha com sucesso. Quantidade atual de linhas: {quantidade_linhas}")
