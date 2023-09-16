markov_chain = {}
markov_list = corpus.split(" ")

n=0
while n < len(markov_list)-1:
    word = markov_list[n].lower().replace('\W+', "")
    if not word in markov_chain.keys():
        markov_chain[word] = []
    if markov_list[n+1]:
        markov_chain[word].append(markov_list[n+1])
    n = n + 1

corpus_words= [word for word in corpus_words if word != '']

words = list(markov_chain.keys())
distinct_words = list(set(words))
word_index_dict = {word: i for i, word in enumerate(distinct_words)}
distinct_words_count = len(list(set(words)))