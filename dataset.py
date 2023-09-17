from corpus import load_corpus

def dataset_init():
    markov_list = load_corpus(["corpus.txt"]).split(" ")
    markov_list= [word for word in markov_list if word != '']
    return markov_list