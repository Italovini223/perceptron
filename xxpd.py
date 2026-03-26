import os
import pandas as pd

LOCAL_PATH = os.path.join(os.getcwd(), './datasets/treinamento.xlsx')

df_treinamento = pd.read_excel(LOCAL_PATH)

# dados_treinamento = [
#     [-0.6508, 0.1097, 4.0009, -1.0], [-1.4492, 0.8896, 4.4005, -1.0],
#     [2.0850, 0.6876, 12.0710, -1.0], [0.2626, 1.1476, 7.7985, 1.0],
#     [0.6418, 1.0234, 7.0427, 1.0], [0.2569, 0.6730, 8.3265, -1.0],
#     [1.1155, 0.6043, 7.4446, 1.0], [0.0914, 0.3399, 7.0677, -1.0],
#     [0.0121, 0.5256, 4.6316, 1.0], [-0.0429, 0.4660, 5.4323, 1.0],
#     [0.4340, 0.6870, 8.2287, -1.0], [0.2735, 1.0287, 7.1934, 1.0],
#     [0.4839, 0.4851, 7.4850, -1.0], [0.4089, -0.1267, 5.5019, -1.0],
#     [1.4391, 0.1614, 8.5843, -1.0], [-0.9115, -0.1973, 2.1962, -1.0],
#     [0.3654, 1.0475, 7.4858, 1.0], [0.2144, 0.7515, 7.1699, 1.0],
#     [0.2013, 1.0014, 6.5489, 1.0], [0.6483, 0.2183, 5.8991, 1.0],
#     [-0.1147, 0.2242, 7.2435, -1.0], [-0.7970, 0.8795, 3.8762, 1.0],
#     [-1.0625, 0.6366, 2.4707, 1.0], [0.5307, 0.1285, 5.6883, 1.0],
#     [-1.2200, 0.7777, 1.7252, 1.0], [0.3957, 0.1076, 5.6623, -1.0],
#     [-0.1013, 0.5989, 7.1812, -1.0], [2.4482, 0.9455, 11.2095, 1.0],
#     [2.0149, 0.6192, 10.9263, -1.0], [0.2012, 0.2611, 5.4631, 1.0]
# ]

# # Cria um DataFrame a partir dos dados fornecidos e substitui as colunas
# df_dados = pd.DataFrame(dados_treinamento, columns=['x1', 'x2', 'x3', 'd'])

# # Garante que as colunas existam em df_treinamento
# for col in ['x1', 'x2', 'x3', 'd']:
#     if col not in df_treinamento.columns:
#         df_treinamento[col] = pd.NA

# min_len = min(len(df_treinamento), len(df_dados))

# # Substitui as linhas correspondentes
# df_treinamento.loc[:min_len-1, ['x1', 'x2', 'x3', 'd']] = df_dados.loc[:min_len-1, ['x1', 'x2', 'x3', 'd']].values

# # Se houver mais linhas em df_dados, anexa as extras
# if len(df_dados) > len(df_treinamento):
#     df_extra = df_dados.iloc[len(df_treinamento):].reset_index(drop=True)
#     df_treinamento = pd.concat([df_treinamento, df_extra], ignore_index=True)

# # Salva de volta no arquivo Excel
# df_treinamento.to_excel(LOCAL_PATH, index=False)
# print(f"Substituídas colunas x1,x2,x3,d e salvo em {LOCAL_PATH}")









# cria o plainha sem d 

if __name__ == '__main__':
	out_path = os.path.join(os.getcwd(), './datasets/treinamento_sem_d.xlsx')

	# Cria uma cópia do DataFrame e zera a coluna 'd'
	df_sem_d = df_treinamento.copy()
	df_sem_d['d'] = pd.NA

	# Salva o arquivo de saída
	df_sem_d.to_excel(out_path, index=False)
	print(f"Arquivo criado por xxpd.py: {out_path}")

