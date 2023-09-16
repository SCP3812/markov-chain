#code partially adapted from Striking Loo under idfuckingk liscense https://gist.github.com/StrikingLoo
import random
from dataset import dataset_init
from init_matrix import initialize_matrix

markov_list = dataset_init()
distinct_words = list(set(markov_list))
next_after_k_words_matrix = initialize_matrix(markov_list, distinct_words)

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
stochastic_chain("the world")
