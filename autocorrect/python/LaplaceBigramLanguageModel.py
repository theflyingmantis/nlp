import collections, math

from collections import defaultdict

class LaplaceBigramLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    # TODO your code here
    self.lapunigramCounts = collections.defaultdict(lambda: 0)
    self.bigrams=collections.defaultdict(lambda: defaultdict(lambda: 0))
    self.total = 0
    self.vocab=set([])
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    for sentence in corpus.corpus:
      for datum in sentence.data:  
        token = datum.word
        #print token
        if token == "<s>":
            lastword = token
            continue
        if token == "</s>":
            continue
        self.bigrams[lastword][token] = self.bigrams[lastword][token] + 1
        self.vocab.add(token)
        self.lapunigramCounts[token] = self.lapunigramCounts[token] + 1
        self.total += 1
        lastword = token

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    score = 0.0 
    first_word = True
    for token in sentence:
        if first_word == True:
            previous = token
            first_word = False
            continue
        count = self.bigrams[previous][token] + 1 # +1 for Laplace Smoothing
        score += math.log(count)
        previous_words = self.lapunigramCounts[previous]
        score -= math.log(previous_words + len(self.vocab))
        previous = token
    return score
