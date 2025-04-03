import pandas as pd

# Carrega o arquivo Excel
nome_arquivo = r"C:\Users\wilgner.oliveira\PycharmProjects\CodigosPRINCIPAIS\Data-main\Finalizados\Consolidados\geral ltda\GERAL\tira duplicada de ura.xlsx"# Substitua pelo caminho do seu arquivo Excel
dados = pd.read_excel(nome_arquivo)

# Nome da coluna que deseja verificar as repetições
nome_coluna = 'Telefone sem 82'  # Substitua pelo nome da sua coluna

# Remove os números repetidos, mantendo apenas o último
dados_sem_repetidos = dados.drop_duplicates(subset=nome_coluna, keep='last')

# Salva os dados sem repetição em um novo arquivo Excel
  # Substitua pelo nome do novo arquivo Excel
dados_sem_repetidos.to_excel( r"C:\Users\wilgner.oliveira\PycharmProjects\CodigosPRINCIPAIS\Data-main\Finalizados\Consolidados\geral ltda\GERAL\tira duplicada de ura.xlsx", index=False)

print("Números repetidos removidos com sucesso e novo arquivo salvo:")

