import pandas as pd

def eliminar_linhas(arquivo_principal, arquivo_linhas_a_remover, coluna_chave, saida):
    """
    Remove linhas do arquivo_principal que estão presentes no arquivo_linhas_a_remover
    com base em uma coluna chave.
    
    Args:
        arquivo_principal (str): Caminho do arquivo principal (CSV ou Excel)
        arquivo_linhas_a_remover (str): Caminho do arquivo com linhas a remover (CSV ou Excel)
        coluna_chave (str): Nome da coluna usada para comparar as linhas
        saida (str): Caminho do arquivo de saída (será salvo como Excel)
    """
    # Função para ler arquivo com tratamento de erros
    def ler_arquivo(arquivo):
        try:
            if arquivo.endswith('.csv'):
                # Tentar ler com diferentes delimitadores e tratamento de erros
                return pd.read_csv(arquivo, delimiter=None, engine='python', on_bad_lines='warn')
            else:
                return pd.read_excel(arquivo)
        except Exception as e:
            print(f"Erro ao ler o arquivo {arquivo}: {str(e)}")
            raise

    # Ler os arquivos
    df_principal = ler_arquivo(arquivo_principal)
    df_remover = ler_arquivo(arquivo_linhas_a_remover)
    
    # Verificar se os DataFrames foram carregados corretamente
    if df_principal.empty or df_remover.empty:
        raise ValueError("Um dos arquivos está vazio ou não foi lido corretamente")
    
    # Verificar se a coluna chave existe em ambos DataFrames
    if coluna_chave not in df_principal.columns or coluna_chave not in df_remover.columns:
        colunas_disponiveis = f"Colunas disponíveis no principal: {df_principal.columns.tolist()}\nColunas disponíveis no remover: {df_remover.columns.tolist()}"
        raise ValueError(f"A coluna '{coluna_chave}' não existe em um dos arquivos\n{colunas_disponiveis}")
    
    # Converter a coluna chave para string para evitar problemas de tipo
    df_principal[coluna_chave] = df_principal[coluna_chave].astype(str)
    df_remover[coluna_chave] = df_remover[coluna_chave].astype(str)
    
    # Obter os valores únicos da coluna chave para remover
    valores_a_remover = set(df_remover[coluna_chave].unique())
    
    # Filtrar o DataFrame principal mantendo apenas linhas não presentes no outro
    df_resultado = df_principal[~df_principal[coluna_chave].isin(valores_a_remover)]
    
    # Salvar o resultado em um novo arquivo Excel
    df_resultado.to_excel(saida, index=False)
    print(f"Arquivo gerado com sucesso: {saida}")
    print(f"Total de linhas original: {len(df_principal)}")
    print(f"Total de linhas removidas: {len(df_principal) - len(df_resultado)}")
    print(f"Total de linhas restantes: {len(df_resultado)}")

# Exemplo de uso
if __name__ == "__main__":
    # Configurações - altere conforme necessário
    arquivo_principal = "Para apagar.csv"      # Arquivo principal
    arquivo_remover = "todas 2 tratado.csv"   # Arquivo com linhas a remover
    coluna_chave = "ID"                       # Coluna usada para comparação
    arquivo_saida = "resultado.xlsx"          # Arquivo de saída
    
    try:
        eliminar_linhas(arquivo_principal, arquivo_remover, coluna_chave, arquivo_saida)
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")
        print("Verifique:")
        print("- Se os nomes dos arquivos estão corretos")
        print("- Se a coluna chave existe em ambos arquivos")
        print("- Se os arquivos não estão corrompidos")
        print("- Se há linhas inconsistentes nos arquivos CSV")