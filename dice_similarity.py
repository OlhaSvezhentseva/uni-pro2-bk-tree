def get_bigrams(word):
    bigrams = set()
    i = 0
    while i < len(word) -1:
        bigrams.add(word[i]+word[i+1])
        i += 1
    return bigrams


def compute_intersection(bigrams1, bigrams2):
    intersect = 0
    for element in bigrams1:
        for bigram in bigrams2:
            if element == bigram:
                intersect += 1
    return intersect


def compute_similarity(word1, word2):
    word_1_bigrams = get_bigrams(word1)
    word_2_bigrams = get_bigrams(word2)
    intersect = compute_intersection( word_1_bigrams, word_2_bigrams)
    return (2 * intersect)/(len(word_1_bigrams) + len(word_2_bigrams))

print(compute_similarity("night", "nacht"))
print(compute_similarity("nanu", "nana"))
print(compute_similarity("nana", "nana"))