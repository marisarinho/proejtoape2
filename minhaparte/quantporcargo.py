import pandas as pd


# !!!!!!!!!!!!!!!!!!!!!!!! 1 ponto !!!!!!!!!!!!!!!!!!!!!!!!!



# lendo o arquivo de cargos 
df = pd.read_csv('minhaparte/cargos.csv', encoding='utf-8', on_bad_lines='skip')

print("Nomes das colunas:", df.columns)

# Contar a quantidade de vezes que aparece cada cargo
df_counts = df['Cargo'].value_counts().reset_index()
df_counts.columns = ['Cargo', 'Quantidade']

print(df_counts)


# Carregar os dois arquivos CSV
arquivo1_df = pd.read_csv('minhaparte/cargos.csv')
arquivo2_df = pd.read_csv('minhaparte/partidos.csv')

# Juntar os DataFrames lado a lado (horizontalmente)
arquivo_junto_df = pd.concat([arquivo1_df, arquivo2_df], axis=1)

# Salvar o resultado em um novo arquivo CSV, separado por ponto e vírgula (;)
arquivo_junto_df.to_csv('minhaparte/arquivo_junto.csv', sep=';', index=False)



# !!!!!!!!!!!!!!!!!!!!!!!!2 ponto!!!!!!!!!!!!!!!!!!!!!!!!!!


# Carregar o arquivo com o separador ';'
arquivo_junto_df = pd.read_csv('minhaparte/arquivo_junto.csv', sep=';', engine='python')


# Remover possíveis espaços extras das colunas
arquivo_junto_df.columns = arquivo_junto_df.columns.str.strip()
# acessando apenas as linhas que contem os prefeitos
prefeitos_df = arquivo_junto_df[arquivo_junto_df['Cargo'].str.upper().str.strip() == 'PREFEITO']

partidos_com_prefeitos_df = prefeitos_df[['NM_PARTIDO']].drop_duplicates()

# Exibir o resultado
print(partidos_com_prefeitos_df)


# !!!!!!!!!!!!!!!!!!!!!!!!!!! 4 ponto !!!!!!!!!!!!!!!!!!!!!!!!!!


arq1_df = pd.read_csv('minhaparte/escolaridade.csv')
arq2_df = pd.read_csv('minhaparte/estadocivil.csv')
arq3_df = pd.read_csv('minhaparte/genero.csv')

arquivo_junto2_df = pd.concat([arq1_df, arq2_df, arq3_df], axis=1)

# Salvar o resultado em um novo arquivo CSV, separado por ponto e vírgula (;)
arquivo_junto2_df.to_csv('minhaparte/arquivo_junto2.csv', sep=';', index=False)
