import collections, math

from collections import defaultdict

class CustomLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    # TODO your code here
    self.lapunigramCounts = collections.defaultdict(lambda: 0)
    self.bigrams=collections.defaultdict(lambda: defaultdict(lambda: 0))
    self.trigrams = collections.defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 0)))
    self.total = 0
    self.vocab=set([])
    self.train(corpus)
  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    for sentence in corpus.corpus:
      lastword = sentence.data[0]
      second_last = sentence.data[1]
      self.bigrams[lastword][second_last] += 1
      self.vocab.add(second_last)
      self.lapunigramCounts[second_last] += 1
      self.total += 1
      for datum in sentence.data[2:]:  
        token = datum.word
        #print token
        if token == "</s>":
            continue
        self.bigrams[second_last][token] += 1
        self.trigrams[lastword][second_last][token] += 1
        self.lapunigramCounts[token] += 1
        self.vocab.add(token)
        self.total += 1
        lastword = second_last
        second_last = token

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    score = 0.0 
    #print self.trigrams["cat"]["quietly"]["ate"]
    p1 = sentence[0]
    p2 = sentence[1]
    for token in sentence[2:]:
        #print token
        count_trigram = self.trigrams[p1][p2][token]
        count_bigram = self.bigrams[p2][token]
        if count_trigram != 0:
            score += math.log(count_trigram) + math.log (0.1)
            score -= math.log(self.bigrams[p1][p2])
        elif count_bigram != 0:
            score += math.log(count_bigram) + math.log (0.3)
            score -= math.log(self.lapunigramCounts[p2])
        else:
            score += math.log(self.lapunigramCounts[token] + 1) + math.log (0.6)
            score -= math.log(self.total+len(self.vocab))
        p1 = p2
        p2 = token
    return score
