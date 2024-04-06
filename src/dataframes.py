import pandas as pd

#dataframe ja filtrado só com os casos de AVC
data_AVC = pd.read_csv('src/data.csv')
data_AVC = data_AVC.rename(columns={'Residence_type': 'residence_type'})
data_AVC = data_AVC.sort_values(by=['age'], kind='stable')
data_AVC['age'] = data_AVC['age'].astype(int)
data_AVC = data_AVC[data_AVC['stroke'] == 1]
#print(data_AVC)