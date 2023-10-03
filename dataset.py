from corpus import load_corpus

def dataset_init():
    markov_list = load_corpus(["Revelations_KJV.txt", "azathoth.txt", "patricia_taxxon.txt"]).split(" ")
    markov_list= [word for word in markov_list if word != '']
    return markov_list
