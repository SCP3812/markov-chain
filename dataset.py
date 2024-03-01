from corpus import load_corpus

def dataset_init():
    markov_list = load_corpus(["frankenstein_radio_controls.txt", "Deathcon.txt", "fanged_noumena.txt", "jerUSAlem.txt", "King_James_Bible.txt"]).split(" ")
    markov_list= [word for word in markov_list if word != '']
    return markov_list
