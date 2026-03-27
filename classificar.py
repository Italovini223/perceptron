import pandas as pd
import os

PATH = os.path.join(os.getcwd(), './datasets/validacao.xlsx')
df_validacao = pd.read_excel(PATH)

def validar(pesos, limiarDeAtivacao, treino):
  df_validacao[f'Y_T{treino}'] = pd.NA 

  for index, row in df_validacao.iterrows():
    x = [row['x1'], row['x2'], row['x3']]
    
        
    U = sum(w * xi for w, xi in zip(pesos, x)) - limiarDeAtivacao
    if U >= 0:
      y = 1
    else:
      y = -1
        
    df_validacao.at[index, f'Y_T{treino}'] = y
  
  df_validacao.to_excel(PATH, index=False)

