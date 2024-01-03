from dataset import dataset_init
from scipy.sparse import dok_matrix

markov_list = dataset_init()
distinct_words = list(set(markov_list))
word_index_dict = {word: i for i, word in enumerate(distinct_words)}

def initialize_matrix(words, distinct_words):
    k = 3
    sets_of_k_words = [ ' '.join(words[i:i+k]) for i, _ in enumerate(words[:-k]) ]
    sets_count = len(list(set(sets_of_k_words)))
    next_after_k_words_matrix = dok_matrix((sets_count, len(distinct_words)))

    distinct_sets_of_k_words = list(set(sets_of_k_words))
    k_words_index_dict = {word: i for i, word in enumerate(distinct_sets_of_k_words)}

    for i, word in enumerate(sets_of_k_words[:-k]):

        word_sequence_idx = k_words_index_dict[word]
        next_word_idx = word_index_dict[words[i+k]]
        next_after_k_words_matrix[word_sequence_idx, next_word_idx] +=1

    return next_after_k_words_matrix, k_words_index_dict
