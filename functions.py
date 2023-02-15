special_chars = ["?", "...", "@", "¿", ",", "'", "\"", "#", "&", "."]

def __clean_word_item( word):
    for s_char in special_chars:
        word = word.replace(s_char, "")
    return word.lower()

def __is_it_formed_by_special_chars( word):
        i = 0
        while i<len(special_chars) and len(word)>0:
            word = word.replace(special_chars[i], "")
            i += 1
        return len(word)!=0

def clean_data(filename):
    file_obj = open(filename, "r")
    file_data = file_obj.read()
    clean_dataset = []
    for linea in file_data:
        words = [__clean_word_item(word.lower()) for word in linea.strip().split(" ") if __is_it_formed_by_special_chars(word)]
        clean_dataset.append(words)
    return clean_dataset
