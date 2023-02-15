# task 1 (sin libreria)
class HamSPam():
    
    def __init__(self, text, seed, classes, train = 0.8 ) -> None:
        self.text = text
        self.train = train if train<1 else 0.8
        self.special_chars = ["?", "...", "@", "¿", ",", "'", "\"", "#", "&", "."]
        self.training_dataset, self.test_dataset = self.__clean_format_data(text, seed)
        self.word_count = {}
        self.class_count = {}
        self.total_words = 0
        self.classes = classes
    
    def __is_it_formed_by_special_chars(self, word):
        i = 0
        while i<len(self.special_chars) and len(word)>0:
            word = word.replace(self.special_chars[i], "")
            i += 1
        return len(word)!=0

    def __clean_format_data(self, text, seed):
        
        def __find_pseudorandom_in_list(seed, dataset, subdataset_length):
            seed = seed%len(dataset)
            rest_dataset = dataset
            rand_subdataset = []
            i = 0
            while len(rand_subdataset)<subdataset_length: 
                rand_subdataset.append(rest_dataset.pop((seed+(i**2))%len(rest_dataset)))
                i += 1
            return rand_subdataset, rest_dataset
        
        dataset = text.strip().split("\n")
        train_dataset_len = int(len(dataset)*self.train)
        test_dataset_len = len(dataset)-train_dataset_len
        
        training_dataset = []
        test_dataset = []

        if train_dataset_len<test_dataset_len:
            training_dataset, test_dataset = __find_pseudorandom_in_list(seed, dataset, train_dataset_len)
        else:
            test_dataset, training_dataset = __find_pseudorandom_in_list(seed, dataset, test_dataset_len)
        
        return training_dataset, test_dataset

    def __clean_word_item(self, word):
        for s_char in self.special_chars:
            word = word.replace(s_char, "")
        return word.lower()
    
    def train_text(self):
        word_count = {}
        class_count = {}
        for cls in self.classes: 
            word_count[cls] = {}
            class_count[cls] = 0
        total_words = 0
        lines = self.training_dataset
        for line in lines:
            cls, doc = line.strip().split("\t")
            words = [self.__clean_word_item(word.lower()) for word in doc.strip().split(" ") if self.__is_it_formed_by_special_chars(word)]
            class_count[cls] += 1
            total_words += len(words)
            for word in words:
                if word not in word_count[cls]:
                    word_count[cls][word] = 1
                else:
                    word_count[cls][word] += 1
        self.word_count, self.class_count, self.total_words = word_count, class_count, total_words
        return word_count, class_count, total_words

    def classify_text(self, text):
        prob = {}
        for cls in self.classes:
            prob[cls] = 1.0
            # Separar cada palabra asi se vuelve minuscula y se lee
            words = [self.__clean_word_item(word.lower()) for word in text.strip().split(" ") if self.__is_it_formed_by_special_chars(word)]
            for word in words:
                if word in self.word_count[cls]:
                    prob[cls] *= (self.word_count[cls][word] + 1) / (self.class_count[cls] + self.total_words)
                else:
                    prob[cls] *= 1 / (self.class_count[cls] + self.total_words)
            prob[cls] = prob[cls] * self.class_count[cls] / len(self.classes)
        return max(prob, key=prob.get)

    def testing_dataset(self, dataset):
        confusion_matrix = [[0, 0], [0, 0]]
        total = 0
        aciertos = 0
        # ham possitive; spam possitive
        for sentence in dataset:
            cls, doc = sentence.strip().split("\t")
            classify = self.classify_text(doc)
            total += 1
            
            if cls=="ham":
                if classify==cls: #positive, positive -> 0, 0
                    confusion_matrix[0][0] += 1
                    aciertos += 1
                else:
                    confusion_matrix[0][1] += 1
            else:
                if classify==cls: #positive, positive -> 0, 0
                    confusion_matrix[1][1] += 1
                    aciertos += 1
                else:
                    confusion_matrix[1][0] += 1
        return confusion_matrix, aciertos/total
    
