'''
Pandas - Dataframe:
É uma tabela de dados.

Tupla ------> () -> Imutável
    tupla_exemplo = (1, 2, 3, 4, 5)
Lista ------> [] -> Mutável
    lista_exemplo = [1, 2, 3, 4, 5]
Dicionário -> {} -> Mutável
    dicionario_exemplo = {
        "chave 1" : 10,
        "chave 2" : 20,
        "chave 3" : 30
    }
'''
# EXIBIR TIPOS DE TUPLA, LISTA E DICIONÁRIO:
print('\nTupla:', type( (1, 2, 3) ))
print('Lista:', type( [1, 2, 3] ))
print('Dicionário:', type( {1 : 'Leandro', 2 : 'João', 3 : 'Michel'} ))

# IMPORTAR PANDAS COMO PD:
import pandas as pd

# CRIAR DATAFRAME:
planilha = 'dados.xlsx'
dataframe = pd.read_excel(planilha)

# EXIBIR DATAFRAME:
print('\nDATAFRAME:\n', dataframe, '\n')

# EXIBIR SOMENTE OS 2 PRIMEIROS:
print('\nDATAFRAME 2 PRIMEIROS:\n', dataframe.head(2), '\n')

# CRIAR COLUNA "VALOR" COM VALOR "5":
dataframe['valor'] = 5
print('\nCRIAR COLUNA "VALOR" COM VALOR "5":\n', dataframe, '\n')

# MUDAR VALOR PARA "10" TODO CAMPO QUE TIVER "LEANDRO":
dataframe.loc[dataframe['nome'] == 'Leandro', 'valor'] = 10
print('\nMUDAR VALOR PARA "10" TODO CAMPO QUE TIVER "LEANDRO":\n', dataframe, '\n')

# EXIBIR INFORMAÇÕES DO DATAFRAME:
print('\nEXIBIR INFORMAÇÕES DO DATAFRAME:')
dataframe.info()
