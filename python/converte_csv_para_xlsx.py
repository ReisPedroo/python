import pandas as pd
import os

# colocar aqui onde os arquivos para ser convertidos estão
caminhos_csv = [
    f"caminho do arquivo"
    ]

for caminho in caminhos_csv:

    try:
        pasta_para_salvar = f'pasta onde ira salvar o arquivo'
        nome_xlsx = os.path.basename(caminho).replace('.csv', '.xlsx')
        caminho_xlsx = os.path.join(pasta_para_salvar, nome_xlsx)

        # Lendo o arquivo .csv
        df = pd.read_csv(caminho, encoding='latin-1', sep=';')

        # Salvando o arquivo no formato .xlsx
        df.to_excel(caminho_xlsx, index=False)
    except Exception as e:
        print(f'Erro ao converter o arquivo {caminho}: {e}')
