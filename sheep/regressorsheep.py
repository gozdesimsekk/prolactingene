import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
import numpy as np

data = pd.read_excel("alldata_sheep.xlsx")
data = data.drop(['Sample', 'Breed', 'Animal', '219'], axis=1)
genotype_columns = ['47845667', '47846990', '47847030', '47847087', '47847605',
       '47848937', '47848947', '47848956', '47848967', '47849004', '47849959',
       '47850077', '47850195', '47850213', '47850553']
data = data.rename(columns={'LSV (kg)': 'lsv'})


data['lsv'] = np.log(data['lsv'])
data['lsv'] = np.round(data['lsv'], 3)


for column in genotype_columns:
    # Her genotip sütunu için 0|0'ı 0, 0|1'ı 1, 1|0'ı 2 ve 1|1'i 3 olarak kodladık
    data[column] = data[column].apply(lambda x: 0 if x == '0|0' else 1 if x == '0|1' else 2 if x == '1|0' else 3)


# Eşleşen satırları bulma
duplicates = data[data.duplicated()]

# İlk eşleşen satırı silme
data.drop_duplicates(inplace=True)

#data.to_csv('labelled2.tsv', sep='\t', index=False)

""" VERİ DAĞILIMINI DAHA DÜZENLİ HALE GETİRMEYE ÇALIŞTIM"""

"""rows_to_drop = data[data['lsv'] == 4.605].index[:16]
data = data.drop(rows_to_drop)
"""
#hepsinden kaç tane olduğunu eşitliği kontrol etmek için baktık
lsv_counts = data['lsv'].value_counts()
print(lsv_counts)

X = data[genotype_columns]
y = data["lsv"]

# split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# create a neural network model
model = Sequential()
model.add(Dense(15, input_dim=15, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='linear'))

# compile the model
model.compile(loss='mean_squared_error', optimizer='adam')

# fit the model on the training data
model.fit(X_train, y_train, epochs=100, batch_size=10)

# evaluate the model on the test data
scores = model.evaluate(X_test, y_test)
print(f'Test loss: {scores}')

# perform 5-fold cross-validation
n_splits = 5
kf = KFold(n_splits=n_splits)
fold = 1
for train_index, test_index in kf.split(X):
    print(f'Fold {fold}/{n_splits}')
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]
    model.fit(X_train, y_train, epochs=100, batch_size=10)
    scores = model.evaluate(X_test, y_test)
    print(f'Test loss: {scores}')
    fold += 1

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean squared error: {mse}')
print(f'MAE: {mae}')
print(f'R^2: {r2}')

"""Mean squared error: 0.11301649416385791
MAE: 0.2952675226211549
R^2: 0.11933598145531654"""
