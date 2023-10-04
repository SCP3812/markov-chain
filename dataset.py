from corpus import load_corpus

def dataset_init():
    markov_list = load_corpus(["ghosts_of_my_life.txt", "ghosts-of-my-life-2.txt", "ghosts-of-my-life-3.txt", "patricia_taxxon.txt"]).split(" ")
    markov_list= [word for word in markov_list if word != '']
    return markov_list
