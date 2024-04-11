import pandas as pd

#dataframe geral do csv
df = pd.read_csv('src/data.csv')
print(df)

#algumas configurações
df = df.sort_values(by=['age'], kind='stable')
df = df.rename(columns={'Residence_type': 'residence_type'})
pd.options.display.float_format = '{:.2f}'.format
df['age'] = df['age'].astype(int)
print(df)
#Valores ordenados e transformados em int para facilitar calculos e análises

#aplicando filtro de idade
#Tirando todas as pessoas com idades superiores a 79 para facilitar a distribuição das frequências
df_filtro = df.query('age < 80')
print(df_filtro)

#aplicando filtro de casos de AVC 
data_AVC = df[df['stroke'] == 1]
print(data_AVC)

##correlacao entre fumantes, doenca cardiaca e AVC
df_correlacao = (df['heart_disease'] == 1) & (df['smoking_status'] == "smoked") & (df['stroke'] == 1)
print(df_correlacao)

