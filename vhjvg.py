import pandas as pd
import random
import os

dados_treinamento = [
    [-0.6508, 0.1097, 4.0009, -1.0], [-1.4492, 0.8896, 4.4005, -1.0],
    [2.0850, 0.6876, 12.0710, -1.0], [0.2626, 1.1476, 7.7985, 1.0],
    [0.6418, 1.0234, 7.0427, 1.0], [0.2569, 0.6730, 8.3265, -1.0],
    [1.1155, 0.6043, 7.4446, 1.0], [0.0914, 0.3399, 7.0677, -1.0],
    [0.0121, 0.5256, 4.6316, 1.0], [-0.0429, 0.4660, 5.4323, 1.0],
    [0.4340, 0.6870, 8.2287, -1.0], [0.2735, 1.0287, 7.1934, 1.0],
    [0.4839, 0.4851, 7.4850, -1.0], [0.4089, -0.1267, 5.5019, -1.0],
    [1.4391, 0.1614, 8.5843, -1.0], [-0.9115, -0.1973, 2.1962, -1.0],
    [0.3654, 1.0475, 7.4858, 1.0], [0.2144, 0.7515, 7.1699, 1.0],
    [0.2013, 1.0014, 6.5489, 1.0], [0.6483, 0.2183, 5.8991, 1.0],
    [-0.1147, 0.2242, 7.2435, -1.0], [-0.7970, 0.8795, 3.8762, 1.0],
    [-1.0625, 0.6366, 2.4707, 1.0], [0.5307, 0.1285, 5.6883, 1.0],
    [-1.2200, 0.7777, 1.7252, 1.0], [0.3957, 0.1076, 5.6623, -1.0],
    [-0.1013, 0.5989, 7.1812, -1.0], [2.4482, 0.9455, 11.2095, 1.0],
    [2.0149, 0.6192, 10.9263, -1.0], [0.2012, 0.2611, 5.4631, 1.0]
]

LOCAL_PATH = os.path.join(os.getcwd(), './datasets/treinamento.xlsx')

df_treinamento = pd.read_excel(LOCAL_PATH)

epocas = 0;
pesos = [random.uniform(-1, 1) for _ in range(3)]
limiarDeAtivacao = random.uniform(-1, 1);
taxaDeAprendizagem = 0.01;


for i in range(0, 3):    
    pesos[i] = random.uniform(-1, 1);


while epocas < 1000:
    epocas += 1;
    erro = False;



    # `dados_treinamento` é uma lista de listas [x1, x2, x3, d]
    for index, row in enumerate(dados_treinamento):
        x = [row[0], row[1], row[2]]
        d = row[3]

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
        break

if epocas == 1000:
    print('Limite de épocas atingido. Pesos finais: ', pesos)