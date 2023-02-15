from ham_spam import HamSPam

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

conf_matrix_test = S.testing_dataset(S.test_dataset) 
conf_matrix_train = S.testing_dataset(S.training_dataset)
print('a')
