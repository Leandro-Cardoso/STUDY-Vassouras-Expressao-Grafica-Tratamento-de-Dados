'''
TRATAMENTO DE DADOS:
'''

import pandas as pd
from os import system

system('clear')

df = pd.read_csv('comerciante.csv')
print(df.head(10))

# SIMPLIFICAÇÂO DE NOME DAS COLUNAS:
df.rename(columns = {
    'Carimbo de data/hora' : 'Data/hora',
    'Nome completo do comerciante' : 'Nome',
    'Nome do comércio' : 'Comércio',
    'Como você preferiria gerenciar os seus fornecedores?' : 'Plataforma',
    'Qual a dificuldade para encontrar novos fornecedores?' : 'Novos fornecedores',
    'Quando é necessário renovar os estoques, qual a disponibilidade dos produtos junto aos fornecedores?' : 'Disponibilidade dos produtos',
    'Quanto o valor o produto influencia na desistência da compra junto ao fornecedor?' : 'Influencia do valor do produto',
    'Deseja receber feedback dessa pesquisa?' : 'Receber feedback'
}, inplace = True)
print(df.head(10))

# SALVAR:
df.to_csv('dado-tratado.csv', index = False)
