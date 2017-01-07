from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

example_words = ["rode","ride","riding","rides","rid"]

for w in example_words:
    print(ps.stem(w))
