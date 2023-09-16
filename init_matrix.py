def stochastic_matrix(rows, columns):
    shell = []
    matrix = []
    i = 0
    while i < rows:
        n = 0
        matrix.append(shell)
        print(matrix[i])
        i = i + 1
    return matrix

def initialize_matrix():
    k = 2
    sets_of_k_words = [ ' '.join(words[i:i+k]) for i, _ in enumerate(words[:-k]) ]
    sets_count = len(list(set(sets_of_k_words)))
    print(sets_count)
    print(len(distinct_words))
    next_after_k_words_matrix = stochastic_matrix(sets_count, len(distinct_words))

    distinct_sets_of_k_words = list(set(sets_of_k_words))
    k_words_idx_dict = {word: i for i, word in enumerate(distinct_sets_of_k_words)}

    word = words[random.randint(0, len(words)-1)]

    for i, word in enumerate(sets_of_k_words[:-k]):

        word_sequence_idx = k_words_idx_dict[word]
        next_word_idx = word_idx_dict[corpus_words[i+k]]
        next_after_k_words_matrix[word_sequence_idx, next_word_idx] +=1
    
