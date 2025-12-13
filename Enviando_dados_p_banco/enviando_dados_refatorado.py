import pandas as pd
import psycopg2

caminho_do_arquivo = r"C:\Users\jabul\OneDrive\Desktop\FPScoders\Python_Para _Data_Science\Arquivo_json\V_OCORRENCIA_AMPLA.json"
df = pd.read_json(caminho_do_arquivo, encoding='utf-8-sig')


# Seleção das colunas
colunas = ["Numero_da_Ocorrencia", "Classificacao_da_Ocorrência",
           "Data_da_Ocorrencia", "Municipio", "UF", "Regiao", "Nome_do_Fabricante"]
df = df[colunas]  # Exibe os dados da colunas em data frames
df.rename(columns={
          'Classificacao_da_Ocorrência': 'Classificacao_da_Ocorrencia'}, inplace=True)


dbname = 'python'
user = 'postgres'
password = '6425'
host = 'localhost'
port = '5432'


conexao = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host, port=port)
cursor = conexao.cursor()

cursor.execute(" delete from public.Ocorrencias_Aeronauticas")


# Carregando os dados no banco de dados

for indice, coluna_df in df.iterrows():
    cursor.execute(""" insert into public.Ocorrencias_Aeronauticas (
                   
                 Numero_da_Ocorrencia,
                 Classificacao_da_Ocorrencia,
                 Data_da_Ocorrencia, 
                 Municipio,
                 UF, 
                 Regiao, 
                 Nome_do_Fabricante
                ) VALUES (%s,%s,%s,%s,%s,%s,%s)



""", (

        coluna_df["Numero_da_Ocorrencia"],
        coluna_df["Classificacao_da_Ocorrencia"],
        coluna_df["Data_da_Ocorrencia"],
        coluna_df["Municipio"],
        coluna_df["UF"],
        coluna_df["Regiao"],
        coluna_df["Nome_do_Fabricante"]





    )




    )


conexao.commit()
cursor.close()
conexao.close()
