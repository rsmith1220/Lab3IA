# task 1 (sin libreria)

def train_text(text, classes):
    word_count = {}
    class_count = {}
    for cls in classes:
        word_count[cls] = {}
        class_count[cls] = 0
    total_words = 0
    lines = text.strip().split("\n")
    for line in lines:
        cls, doc = line.strip().split("\t")
        words = [word.lower() for word in doc.strip().split(" ")]
        class_count[cls] += 1
        total_words += len(words)
        for word in words:
            if word not in word_count[cls]:
                word_count[cls][word] = 1
            else:
                word_count[cls][word] += 1
    return word_count, class_count, total_words

def classify_text(text, classes, word_count, class_count, total_words):
    prob = {}
    for cls in classes:
        prob[cls] = 1.0
        # Separar cada palabra asi se vuelve minuscula y se lee
        words = [word.lower() for word in text.strip().split(" ")]
        for word in words:
            if word in word_count[cls]:
                prob[cls] *= (word_count[cls][word] + 1) / (class_count[cls] + total_words)
            else:
                prob[cls] *= 1 / (class_count[cls] + total_words)
        prob[cls] = prob[cls] * class_count[cls] / len(classes)
    return max(prob, key=prob.get)


# opening the file
file_obj = open("entrenamiento.txt", "r")
  
# reading the data from the file
file_data = file_obj.read()
  
# splitting the file data into lines
lines = file_data.splitlines()
# print(lines)
# file_obj.close()

classes = ["ham", "spam"]

word_count, class_count, total_words = train_text(file_data, classes)


#se lee linea por linea y lo calsifica si es ham o spam
i=0
while i<10:
    
    print(classify_text(lines[i], classes, word_count, class_count, total_words))
    i+=1