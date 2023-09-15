#code partially adapted from Striking Loo under idfuckingk liscense https://gist.github.com/StrikingLoo
import random

corpusium = open("corpus.txt", "r")
corpus = corpusium.read()
corpusium.close()

def transition_matrix(corpus_words):
    pass

def Markovian(markov): 
    markov_chain = {}
    markov_list = markov.split(" ")

    n=0
    while n < len(markov_list)-1:
        word = markov_list[n].lower().replace('\W+', "")
        if not word in markov_chain.keys():
            markov_chain[word] = []
        if markov_list[n+1]:
            markov_chain[word].append(markov_list[n+1])
        n = n + 1 
    words = list(markov_chain.keys())
    distinct_words = list(set(words))
    word_index_dict = {word: i for i, word in enumerate(distinct_words)}
    distinct_words_count = len(list(set(words)))
    k = 2
    sets_of_k_words = [ ' '.join(words[i:i+k]) for i, _ in enumerate(words[:-k]) ]
    sets_count = len(list(set(sets_of_k_words)))
    word = words[random.randint(0, len(words)-1)]
    result = ""

    for i in words:
        result = result + word + " "
        newWord = markov_chain[word][random.randint(0, len(markov_chain[word])-1)]
        word = newWord

        if not word or not word in markov_chain:
            word = words[random.randint(0, len(words)-1)]
    return result

# example use    
print(Markovian(corpus))
