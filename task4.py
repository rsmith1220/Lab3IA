import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

from functions import clean_data

#Cargamos los datos limpios
matrix = clean_data("entrenamiento.txt")
df = pd.DataFrame(matrix)
df.to_csv('nuevo.csv', index=False)
#Cargamos los datos limpios
data = pd.read_csv('nuevo.csv', header=None)

# Split the data into features (message words) and target variable (ham/spam labels)
X = data.iloc[:, 1:]
y = data.iloc[:, 0]

# Convert the text data into numerical features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X.apply(lambda x: ' '.join(str(word) for word in x), axis=1))

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Naive Bayes classifier with Laplace smoothing
classifier = MultinomialNB(alpha=1)

# Fit the classifier to the training data
classifier.fit(X_train, y_train)

# Test the accuracy of the classifier on the test data
accuracy = classifier.score(X_test, y_test)

print("Accuracy:",accuracy)