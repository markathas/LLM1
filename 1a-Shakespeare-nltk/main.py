import nltk
import time

f = open('/mnt/data/MyDocuments/shakespeare/complete-works.original.txt', mode='r')
sp = f.read()
print('string length:', len(sp))
st = time.time()
tokens = nltk.word_tokenize(sp)
tt = time.time() - st
print('time:', tt)
print('tokens found:', len(tokens))
print(tokens[:100])
