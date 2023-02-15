import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from functions import clean_data
from sklearn.metrics import accuracy_score


def predictHamSpam():
    df = pd.DataFrame(clean_data("entrenamiento.txt"))
    df.to_csv('nuevo.csv', index=False)

    data = pd.read_csv('nuevo.csv', header=None)

    X = data.iloc[:, 1:]
    y = data.iloc[:, 0]

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(X.apply(lambda x: ' '.join(str(word) for word in x), axis=1))

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    classifier = MultinomialNB(alpha=1)

    classifier.fit(X_train, y_train)

    accuracy_test = classifier.score(X_test, y_test)
    accuracy_train = classifier.score(X_train, y_train)
    print("\tAccuracy test: ",accuracy_test)
    print("\tAccuracy train: ",accuracy_train)