import pandas as pd
import random
import os
import matplotlib.pyplot as plt

import resultados
import classificar



LOCAL_PATH = os.path.join(os.getcwd(), './datasets/treinamento.xlsx')
RESULTADOS_PATH = os.path.join(os.getcwd(), './datasets/resultados.xlsx')

df_treinamento = pd.read_excel(LOCAL_PATH)
df_resultados = pd.read_excel(RESULTADOS_PATH)


treinamento = 1
taxaDeAprendizagem = 0.01;

resultados.limpar(df_resultados)


while treinamento  <= 5:
    epocas = 0;
    pesos = [random.uniform(-1, 1) for _ in range(3)]
    limiarDeAtivacao = random.uniform(-1, 1);

    erros_por_epoca = []

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
                erro = True;
                numero_de_erros += 1
                for i in range(len(pesos)):
                    pesos[i] = pesos[i] + taxaDeAprendizagem * (d - y) * x[i]
                
                limiarDeAtivacao = limiarDeAtivacao + taxaDeAprendizagem * (d - y) * (-1)

                
        erros_por_epoca.append(numero_de_erros)

        if not erro:
            pesos_finais = pesos.copy()
            break

    if epocas == 1000:
        print('Limite de épocas atingido. Pesos finais: ', pesos)
    else: 
        print('Treinamento', treinamento, 'concluído em ', epocas, ' épocas. Pesos: ', pesos)

        resultados.preencher_w_finais(df_resultados, treinamento, pesos_finais, epocas, limiarDeAtivacao)
        classificar.validar(pesos_finais, limiarDeAtivacao, treinamento)

        plt.figure(figsize=(19.2, 10.8), dpi=100)
        plt.plot(range(1, len(erros_por_epoca) + 1), erros_por_epoca, color='blue')
        plt.title(f'Evolução do erro - Treinamento {treinamento}')
        plt.xlabel('Épocas')
        plt.ylabel('Número de erros')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f'./graphics/treinamento_{treinamento}.png')
        
    
    treinamento += 1
        


