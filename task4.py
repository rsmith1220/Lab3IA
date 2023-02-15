import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

#Cargamos los datos limpios
data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/spambase/spambase.data', header=None)
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

#Dividimos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Se entrena modelo
model = MultinomialNB()
model.fit(X_train, y_train)

#Se realizan predicciones en conjunto de entrenamiento y prueba
entrenamiento = model.predict(X_train)
prueba = model.predict(X_test)

#Se calcula la exactitud en conjuntos de entrenamiento y prueba
exact_entrenamiento = accuracy_score(y_train, entrenamiento)
exact_prueba = accuracy_score(y_test, prueba)

print('Exactitud en entrenamiento: {:.3f}'.format(exact_entrenamiento))
print('Exactitud en prueba: {:.3f}'.format(exact_prueba))
