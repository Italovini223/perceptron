import os
import pandas as pd


def main():
    local_path = os.path.join(os.getcwd(), './datasets/treinamento.xlsx')
    out_path = os.path.join(os.getcwd(), './datasets/treinamento_sem_d.xlsx')

    df = pd.read_excel(local_path)

    # Se existir a coluna 'd', torna seus valores vazios; caso contrário, adiciona a coluna vazia
    if 'd' in df.columns:
        df_sem_d = df.copy()
        df_sem_d['d'] = pd.NA
    else:
        df_sem_d = df.copy()
        df_sem_d['d'] = pd.NA

    df_sem_d.to_excel(out_path, index=False)
    print(f"Arquivo criado: {out_path}")


if __name__ == '__main__':
    main()
