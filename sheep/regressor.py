import pandas as pd
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import cross_val_score
import numpy as np
data = pd.read_excel("alldata_sheep.xlsx")
data = data.drop(['Sample', 'Breed', 'Animal', '219'], axis=1)
genotype_columns = ['47845667', '47846990', '47847030', '47847087', '47847605', '47848937', '47848947', '47848956', '47848967', '47849004', '47849959', '47850077', '47850195', '47850213', '47850553']
data['LSV (kg)'] = np.log(data['LSV (kg)'])
data['LSV (kg)'] = np.round(data['LSV (kg)'], 3)

for column in genotype_columns:
    # Her genotip sütunu için 0|0'ı 0, 0|1'ı 1, 1|0'ı 2 ve 1|1'i 3 olarak kodladık
    data[column] = data[column].apply(lambda x: 0 if x == '0|0' else 1 if x == '0|1' else 2 if x == '1|0' else 3)


# Eşleşen satırları bulma
duplicates = data[data.duplicated()]

# İlk eşleşen satırı silme
data.drop_duplicates(inplace=True)

data.to_csv('labelled2.tsv', sep='\t', index=False)

print(data)

X = data[genotype_columns]
y = data["LSV (kg)"]

model = MLPRegressor(hidden_layer_sizes=(100), activation='relu', solver='adam', learning_rate='adaptive', alpha=0.001)

scores = cross_val_score(model, X, y, cv=2, scoring="r2")

r2_score = scores.mean()

print("R^2 Score:", r2_score)

