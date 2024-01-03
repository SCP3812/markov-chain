#code partially adapted from Striking Loo under idfuckingk liscense https://gist.github.com/StrikingLoo
import random
from dataset import dataset_init
from init_matrix import initialize_matrix

markov_list = dataset_init()
distinct_words = list(set(markov_list))
next_after_k_words_matrix, k_words_index_dict = initialize_matrix(markov_list, distinct_words)

def sample_next_word_after_sequence(word_sequence, alpha):
    next_word_vector = [] 
    if word_sequence not in k_words_index_dict:
            a = []
            k_words_index_dict[word_sequence] = k_words_index_dict[list(k_words_index_dict.keys())[-1]] + 1
            for column in range(len(distinct_words)):
                a.append(0)
            next_after_k_words_matrix.append(a)
            
    for num in next_after_k_words_matrix[k_words_index_dict[word_sequence]]:
        num = num + alpha
        next_word_vector.append(num)

    if sum(next_word_vector) == 0:
        print(word_sequence)
        #print(next_after_k_words_matrix[k_words_index_dict[word_sequence]])
        #print(k_words_index_dict)
        #print(k_words_index_dict.get("reality"))

    likelihoods = []
    for word in next_word_vector:
        likelihood = word/sum(next_word_vector)
        likelihoods.append(likelihood)
    
    return random.choices(distinct_words, weights=likelihoods)

def stochastic_chain(seed, chain_length, seed_length):
    current_words = seed.split(' ')
    if len(current_words) != seed_length:
        raise ValueError(f'wrong number of words, expected {seed_length}')
    sentence = seed
    
    for _ in range(chain_length):
        sentence+=' '
        next_word = sample_next_word_after_sequence(' '.join(current_words), 0.0001)
        sentence = sentence + next_word[0]
        current_words = current_words[1:]+next_word
    return sentence

# example use
i = 0
while i < 3:  
    print(stochastic_chain("my father is", 150, 3))
    i = i + 1
