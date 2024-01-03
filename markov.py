#code partially adapted from Striking Loo under idfuckingk liscense https://gist.github.com/StrikingLoo
from dataset import dataset_init
from init_matrix import initialize_matrix
from scipy.sparse import dok_matrix, vstack
import numpy as np
import random
from random import random 

def weighted_choice(objects, weights):
    """ returns randomly an element from the sequence of 'objects', 
        the likelihood of the objects is weighted according 
        to the sequence of 'weights', i.e. percentages."""

    weights = np.array(weights, dtype=np.float64)
    sum_of_weights = weights.sum()
    # standardization:
    np.multiply(weights, 1 / sum_of_weights, weights)
    weights = weights.cumsum()
    x = random()
    for i in range(len(weights)):
        if x < weights[i]:
            return objects[i]

markov_list = dataset_init()
distinct_words = list(set(markov_list))
next_after_k_words_matrix, k_words_idx_dict = initialize_matrix(markov_list, distinct_words)

def sample_next_word_after_sequence(word_sequence, alpha):
    if word_sequence not in k_words_idx_dict:
        print("shit")
        a = dok_matrix((1, len(distinct_words)))
        k_words_idx_dict[word_sequence] = k_words_idx_dict[list(k_words_idx_dict.keys())[-1]] + 1
        next_after_k_words_matrix = stack(next_after_k_words_matrix, a)
        print(next_after_k_words_matrix)
    next_word_vector = next_after_k_words_matrix[k_words_idx_dict[word_sequence]] + alpha
    likelihoods = next_word_vector/next_word_vector.sum()
    
    return weighted_choice(distinct_words, likelihoods.toarray())

def stochastic_chain(seed, chain_length, seed_length):
    current_words = seed.split(' ')
    if len(current_words) != seed_length:
        raise ValueError(f'wrong number of words, expected {seed_length}')
    sentence = seed
    
    for _ in range(chain_length):
        sentence+=' '
        next_word = sample_next_word_after_sequence(' '.join(current_words), 0.1)
        sentence+=next_word
        current_words = current_words[1:]+[next_word]
    return sentence

# example use
i = 0
while i < 3:  
    print(stochastic_chain("my father is", 300, 3))
    i = i + 1
