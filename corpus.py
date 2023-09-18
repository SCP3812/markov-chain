def load_corpus(file_names):
    corpus = ""
    for file_name in file_names:
        with open(file_name, 'r') as f:
                corpus+=f.read()
    corpus = corpus.replace('\n',' ')
    corpus = corpus.replace('\t',' ')
    corpus = corpus.replace('“', ' " ')
    corpus = corpus.replace('”', ' " ')
    for spaced in ['.','-',',','!','?','(','—',')']:
        corpus = corpus.replace(spaced, ' {0} '.format(spaced))
    return corpus
