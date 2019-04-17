import nltk
import sys
import nltk.data
from nltk.tokenize import sent_tokenize,word_tokenize

text = sys.stdin.read()
swedish_tokenizer = nltk.data.load('tokenizers/punkt/swedish.pickle')
tokenized_sent = swedish_tokenizer.tokenize(text)
tokenized_word = []
print(tokenized_sent)
for t in tokenized_sent:
    w = word_tokenize(t)
    for ww in w:
        tokenized_word.append(ww)
# print(tokenized_word)
