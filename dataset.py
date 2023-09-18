from corpus import load_corpus

def dataset_init():
    markov_list = load_corpus(["of_the_russe_common_wealth.txt", "fanged_noumena.txt"]).split(" ")
    markov_list= [word for word in markov_list if word != '']
    return markov_list
