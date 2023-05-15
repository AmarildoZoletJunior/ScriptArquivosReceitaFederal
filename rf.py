import pandas as pd
import sqlite3


##programação para tabela estabelecimentos
# DType = {'cnpj__basico': str,'cnpj_ordem': str,'cnpj_dv': str,'identificador_matriz': str,'nome_fantasia': str,'situacao_cadastral': str,'data_situacao_cadastral': str,'motivo_situacao_cadastral': str,'nome_cidade_exterior': str,'pais': str,'data_inicio_atividade': str,'cnae_fiscal_primaria': str,'cnae_fiscal_secundaria': str,'tipo_logradouro': str,'logradouro': str,'numero': str,'complemento': str,'bairro': str,'cep': str,'uf': str,'municipio': str,'ddd_um': str,'telefone_um': str,'ddd_dois': str,'telefone_dois': str,'ddd_fax': str,'fax': str,'correio_eletronico':str,'situacao_especial':str,'data_situacao_especial':str}
# dados_csv = pd.read_csv('estabelecimentos/e9.csv', sep=';',dtype=DType, encoding='latin1',header=None,names=[
#                     'cnpj__basico',
#                     'cnpj_ordem',
#                     'cnpj_dv',
#                     'identificador_matriz' ,
#                     'nome_fantasia',
#                     'situacao_cadastral',
#                     'data_situacao_cadastral',
#                     'motivo_situacao_cadastral',
#                     'nome_cidade_exterior',
#                     'pais',
#                     'data_inicio_atividade',
#                     'cnae_fiscal_primaria',
#                     'cnae_fiscal_secundaria',
#                     'tipo_logradouro',
#                     'logradouro',
#                     'numero',
#                     'complemento',
#                     'bairro',
#                     'cep',
#                     'uf',
#                     'municipio',
#                     'ddd_um',
#                     'telefone_um',
#                     'ddd_dois',
#                     'telefone_dois',
#                     'ddd_fax',
#                     'fax',
#                     'correio_eletronico',
#                     'situacao_especial',
#                     'data_situacao_especial'])
# print(dados_csv)
# con = sqlite3.connect('rf.db')
# cursor = con.cursor()

# cursor.execute('''CREATE TABLE estabelecimentos (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     cnpj__basico TEXT NULL,
#                     cnpj_ordem TEXT NULL,
#                     cnpj_dv TEXT NULL,
#                     identificador_matriz TEXT NULL,
#                     nome_fantasia TEXT,
#                     situacao_cadastral TEXT NULL,
#                     data_situacao_cadastral TEXT NULL,
#                     motivo_situacao_cadastral TEXT NULL,
#                     nome_cidade_exterior TEXT NULL,
#                     pais TEXT NULL,
#                     data_inicio_atividade TEXT NULL,
#                     cnae_fiscal_primaria TEXT NULL,
#                     cnae_fiscal_secundaria TEXT NULL,
#                     tipo_logradouro TEXT NULL,
#                     logradouro TEXT NULL,
#                     numero TEXT NULL,
#                     complemento TEXT NULL,
#                     bairro TEXT NULL,
#                     cep TEXT NULL,
#                     uf TEXT NULL,
#                     municipio TEXT NULL,
#                     ddd_um TEXT NULL,
#                     telefone_um TEXT NULL,
#                     ddd_dois TEXT NULL,
#                     telefone_dois TEXT NULL,
#                     ddd_fax TEXT NULL,
#                     fax TEXT NULL,
#                     correio_eletronico TEXT NULL,
#                     situacao_especial TEXT NULL,
#                     data_situacao_especial TEXT NULL
#                     )''')

# dados_csv.to_sql('estabelecimentos', con, if_exists='append', index=False)

# con.commit()

# con.close()






##programação para tabela empresa

# dados_csv = pd.read_csv('empresas/e0.csv', sep=';', encoding='latin1',header=None, names=['cnpj', 'nome', 'natureza_juridica', 'qualificacao_responsavel', 'capital_social', 'porte', 'ente_federativo'])

# print(dados_csv)

# con = sqlite3.connect('rf.db')

# cursor = con.cursor()

# ###Executa na primeira vez para criar a tabela Empresas
# cursor.execute('''CREATE TABLE empresas (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     cnpj TEXT NULL,
#                     nome TEXT NULL,
#                     natureza_juridica TEXT NULL,
#                     qualificacao_responsavel TEXT NULL,
#                     capital_social TEXT NULL,
#                     porte TEXT NULL,
#                     ente_federativo TEXT NULL
#                     )''')





# dados_csv.to_sql('empresas', con, if_exists='append', index=False)

# con.commit()

# con.close()

