import pandas as pd
import random
import os
import resultados
import validar_treinamento


LOCAL_PATH = os.path.join(os.getcwd(), './datasets/treinamento.xlsx')
TEST_V_PATH = os.path.join(os.getcwd(), './datasets/treinamento_sem_d.xlsx')
RESULTADOS_PATH = os.path.join(os.getcwd(), './datasets/resultados.xlsx')

df_treinamento = pd.read_excel(LOCAL_PATH)
df_treinamento_sem_d = pd.read_excel(TEST_V_PATH)
df_resultados = pd.read_excel(RESULTADOS_PATH)

treinamento = 1


taxaDeAprendizagem = 0.01;

resultados.limpar(df_resultados)


while treinamento  <= 5:
    epocas = 0;
    pesos = [random.uniform(-1, 1) for _ in range(3)]
    limiarDeAtivacao = random.uniform(-1, 1);

    resultados.preencher_w_iniciais(df_resultados, treinamento, pesos, limiarDeAtivacao)


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

                

        if not erro:
            pesos_fiais = pesos.copy()
            break

    if epocas == 1000:
        print('Limite de épocas atingido. Pesos finais: ', pesos)
    else: 
        print('Treinamento', treinamento, 'concluído em ', epocas, ' épocas. Pesos: ', pesos)

        resultados.preencher_w_finais(df_resultados, treinamento, pesos_fiais, epocas, limiarDeAtivacao)

    
    treinamento += 1
        


validar_treinamento.validar(pesos_fiais, limiarDeAtivacao)