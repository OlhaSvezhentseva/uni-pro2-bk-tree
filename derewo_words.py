# Olha Svezhentseva
# 16.08.2022

import pickle
from nltk import word_tokenize


# def extract_words(file_name):
#     words = set()
#     try:
#         with open(file_name, encoding='ISO-8859-15') as file_in:
#             for line in file_in.readlines():
#                 if word_tokenize(line)[0] != "#":
#                     word = word_tokenize(line)[0]
#                     words.add(word)
#     except FileNotFoundError:
#         raise("File not Found")
#     return words






def save_words(words, output_file):
    with open(output_file, "wb") as fp:
        pickle.dump(words, fp)


def open_words(output_file):
    with open(output_file, "rb") as fp:
        words = pickle.load(fp)
    return words

def extract_words(input_file, output_file="words"):
    words = set()
    try:
        with open(input_file, encoding='ISO-8859-15') as file_in:
            for line in file_in.readlines():
                if word_tokenize(line)[0] != "#":
                    word = word_tokenize(line)[0]
                    words.add(word)
    except FileNotFoundError:
        raise("File not Found")
    save_words(words, output_file)
    words = open_words(output_file)
    return list(words)
