from ham_spam import HamSPam
from task4 import predictHamSpam
def main():
    # opening the file
    file_obj = open("entrenamiento.txt", "r")
    
    # reading the data from the file
    file_data = file_obj.read()

    # splitting the file data into lines
    lines = file_data.splitlines()
    # print(lines)
    # file_obj.close()

    classes = ["ham", "spam"]

    S = HamSPam(file_data, 7, classes)

    S.train_text()

    res = (S.classify_text("Those ducking chinchillas"))

    conf_matrix_test, accuracy_test = S.testing_dataset(S.test_dataset) 
    conf_matrix_train, accuracy_train = S.testing_dataset(S.training_dataset)
    print('Resultados con modulo propio')
    print("\tAccuracy test: ",accuracy_test)
    print("\tAccuracy train: ",accuracy_train)
    print('Resultados con librerías externas')
    predictHamSpam()
    print("¿Cual tuvo mejor performance?")
    print("R/ El de sklearn")
    print("¿Por qué?")
    print("R/ Sobre todo por el parametro de ajuste de alpha o que tiene un mejor algorimto para la seleccion aleatorio de datos.\n Nuestra implementacion pseudoaleatoria fue un poco aribtraria")

if __name__=="__main__":
    main()