import pandas as pd
import random
import os


LOCAL_PATH = os.path.join(os.getcwd(), './datasets/treinamento.xlsx')
TEST_V_PATH = os.path.join(os.getcwd(), './datasets/treinamento_sem_d.xlsx')

df_treinamento = pd.read_excel(LOCAL_PATH)
df_treinamento_sem_d = pd.read_excel(TEST_V_PATH)

epocas = 0;
pesos = [random.uniform(-1, 1) for _ in range(3)]
limiarDeAtivacao = random.uniform(-1, 1);
taxaDeAprendizagem = 0.01;


for i in range(0, 3):    
    pesos[i] = random.uniform(-1, 1);


while epocas < 1000:
    epocas += 1;
    erro = False;



    for index, row in df_treinamento.iterrows():
        x = [row['x1'], row['x2'], row['x3']]
        d = row['d']
        
        U = sum(w * xi for w, xi in zip(pesos, x)) - limiarDeAtivacao
        if U >= 0:
            y = 1
        else:
            y = -1
        if y != d:
            erro = True;
            for i in range(len(pesos)):
                pesos[i] = pesos[i] + taxaDeAprendizagem * (d - y) * x[i]
            
            limiarDeAtivacao = limiarDeAtivacao + taxaDeAprendizagem * (d - y) * (-1)

            print(f"Erro na linha {index}: y={y}, d={d}, pesos atualizados: {pesos}, limiar atualizado: {limiarDeAtivacao}")
            

    if not erro:
        pesos_fiais = pesos.copy()
        print('Pesos finais: ', pesos_fiais)
        print('Épocas: ', epocas)
        print('Limiar de ativação final: ', limiarDeAtivacao)
        break

if epocas == 1000:
    print('Limite de épocas atingido. Pesos finais: ', pesos)
else: 
    df_sem_d = df_treinamento_sem_d.copy()
    df_sem_d['d'] = pd.NA


    for i, row in df_treinamento_sem_d.iterrows():
        x = [row['x1'], row['x2'], row['x3']]
        
        U = sum(w * xi for w, xi in zip(pesos_fiais, x)) - limiarDeAtivacao
        if U >= 0:
            y = 1
        else:
            y = -1
        df_sem_d.at[i, 'd'] = y
    
    df_sem_d.to_excel(TEST_V_PATH, index=False)
    print(f"Resultados salvos em {TEST_V_PATH}")
        
for index, row in df_sem_d.iterrows():
    print(f"d de treino {index}: row: {row['d']}")
    print(f"d de teste {index}: row: {df_treinamento.at[index, 'd']}")