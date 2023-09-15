#code partially adapted from Striking Loo under idfuckingk liscense https://gist.github.com/StrikingLoo
import random

corpusium = open("corpus.txt", "r")
corpus = corpusium.read()
corpusium.close()

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
    print(sets_count)
    print(len(distinct_words))
    next_after_k_words_matrix = [[column for column in range(sets_count)] for row in range(len(distinct_words))]
    
    distinct_sets_of_k_words = list(set(sets_of_k_words))
    k_words_idx_dict = {word: i for i, word in enumerate(distinct_sets_of_k_words)}

    word = words[random.randint(0, len(words)-1)]
    result = ""

    for i in words:
        result = result + word + " "
        newWord = markov_chain[word][random.randint(0, len(markov_chain[word])-1)]
        word = newWord

        if not word or not word in markov_chain:
            word = words[random.randint(0, len(words)-1)]
    return result

def sample_next_word_after_sequence(word_sequence, alpha = 0):
    next_word_vector = next_after_k_words_matrix[k_words_idx_dict[word_sequence]] + alpha
    likelihoods = next_word_vector/next_word_vector.sum()
    
    return weighted_choice(distinct_words, likelihoods.toarray())

def stochastic_chain(seed, chain_length=15, seed_length=2):
    current_words = seed.split(' ')
    if len(current_words) != seed_length:
        raise ValueError(f'wrong number of words, expected {seed_length}')
        sentence = seed

    for _ in range(chain_length):
        sentence+=' '
        next_word = sample_next_word_after_sequence(' '.join(current_words))
        sentence+=next_word
        current_words = current_words[1:]+[next_word]
    return sentence

# example use    
print(Markovian(corpus))
