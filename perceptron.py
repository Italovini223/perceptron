import pandas as pd
import random
import os
import matplotlib.pyplot as plt
from math import sqrt
from sklearn.metrics import root_mean_squared_error

import resultados
import classificar
import metricas



LOCAL_PATH = os.path.join(os.getcwd(), './datasets/treinamento.xlsx')
RESULTADOS_PATH = os.path.join(os.getcwd(), './datasets/resultados.xlsx')

df_treinamento = pd.read_excel(LOCAL_PATH)
df_resultados = pd.read_excel(RESULTADOS_PATH)


treinamento = 1
taxaDeAprendizagem = 0.25;


resultados.limpar(df_resultados)


while treinamento  <= 5:
    epocas = 0
    rmse = 0
    pesos = [random.uniform(-1, 1) for _ in range(3)]
    limiarDeAtivacao = random.uniform(-1, 1);


    resultados.preencher_w_iniciais(df_resultados, treinamento, pesos, limiarDeAtivacao)


    while epocas < 1000:
        epocas += 1;
        erro = False;
        numero_de_erros = 0;



        for index, row in df_treinamento.iterrows():
            x = [row['x1'], row['x2'], row['x3']]
            d = row['d']
            
            U = sum(w * xi for w, xi in zip(pesos, x)) - limiarDeAtivacao
            if U >= 0:
                y = 1
            else:
                y = -1
                
            if y != d:
                erro = True
                numero_de_erros += 1
                for i in range(len(pesos)):
                    pesos[i] = pesos[i] + taxaDeAprendizagem * (d - y) * x[i]
                
                limiarDeAtivacao = limiarDeAtivacao + taxaDeAprendizagem * (d - y) * (-1)
            
            

                

        if not erro:
            pesos_finais = pesos.copy()

            for index, row in df_treinamento.iterrows():
                x = [row['x1'], row['x2'], row['x3']]
                d = row['d']
                
                U = sum(w * xi for w, xi in zip(pesos_finais, x)) - limiarDeAtivacao
                if U >= 0:
                    y = 1
                else:
                    y = -1
                df_treinamento.at[index, f'Y_{treinamento}'] = y
            df_treinamento.to_excel(LOCAL_PATH, index=False)

            break

    if epocas == 1000:
        print('Limite de épocas atingido. Pesos finais: ', pesos)
    else: 
        print('Treinamento', treinamento, 'concluído em ', epocas, ' épocas. Pesos: ', pesos)

        resultados.preencher_w_finais(df_resultados, treinamento, pesos_finais, epocas, limiarDeAtivacao)
        classificar.validar(pesos_finais, limiarDeAtivacao, treinamento)

    
        rmse = root_mean_squared_error(df_treinamento['d'], df_treinamento[f'Y_{treinamento}'])


        plt.figure(figsize=(19.2, 10.8), dpi=100)
        plt.scatter(df_treinamento['d'], df_treinamento[f'Y_{treinamento}'], alpha=0.5, color='blue', label='prev')
        plt.plot(range(df_treinamento['d']))
        plt.title(f"RMSE TREINAMENTO {treinamento}: {rmse:.2f}")
        plt.xlabel("valor reais")
        plt.ylabel("valores previstos")
        plt.legend()
        plt.grid(True)
        plt.savefig(f'./graphics/Evolucao_do_erro/treinamento_{treinamento}.png')
        
    
    treinamento += 1
        
metricas.calcular()

