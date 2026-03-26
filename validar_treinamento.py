import pandas as pd
import os

PATH = os.path.join(os.getcwd(), './datasets/treinamento_sem_d.xlsx')
df_treinamento_para_validar = pd.read_excel(PATH)


def validar(pesos, limiarDeAtivacao):
  for index, row in df_treinamento_para_validar.iterrows():
    x = [row['x1'], row['x2'], row['x3']]
    d = row['d']
        
    U = sum(w * xi for w, xi in zip(pesos, x)) - limiarDeAtivacao
    if U >= 0:
      y = 1
    else:
      y = -1
        
    df_treinamento_para_validar.at[index, 'd'] = y
  
  df_treinamento_para_validar.to_excel(PATH, index=False)
  print(f"Treinamento validado e salvo em {PATH}")
