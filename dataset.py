from corpus import load_corpus

def dataset_init():
    markov_list = load_corpus(["frankenstein_radio_controls.txt", "exxon.txt", "fanged_noumena.txt", "designedsystem.txt", "siemens.txt", "patricia_taxxon.txt"]).split(" ")
    markov_list= [word for word in markov_list if word != '']
    return markov_list
