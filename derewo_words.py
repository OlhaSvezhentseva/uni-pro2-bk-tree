import pickle
from nltk import word_tokenize


def extract_words(file_name):
    words = set()
    try:
        with open(file_name, encoding='ISO-8859-15') as file_in:
            for line in file_in.readlines():
                if word_tokenize(line)[0] != "#":
                    word = word_tokenize(line)[0]
                    words.add(word)
    except FileNotFoundError:
        raise("File not Found")
    return words

# words = extract_words("derewo-v-ww-bll-250000g-2011-12-31-0.1.txt")
# print(len(words))

# Pickling

# with open("words2", "wb") as fp:
#     pickle.dump(words, fp)



# Unpickling

with open("words2", "rb") as fp:   # Unpickling
    words = pickle.load(fp)

