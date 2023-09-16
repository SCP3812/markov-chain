from corpus import load_corpus

def dataset_init():
    markov_list = load_corpus(["corpus.txt"]).split(" ")

    markov_list= [word for word in markov_list if word != '']

    word_index_dict = {word: i for i, word in enumerate(distinct_words)}
    distinct_words_count = len(list(set(corpus_list)))
    return markov_list